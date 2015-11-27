# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['zhanzhengcelue', 'dongzuoqiangzhan', 'saichetiyu',
         'wangyouRPG', 'qipaizhuoyou', 'gedoukuaida', 
         'ertongyizhi', 'xiuxianchuangyi', 'feixingkongzhan',
         'paokuchuangguan', 'tafangmigong', 'monijingying']

def extract(page, cate, bias):
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        searchUpdate(soup, 'applist', 'home', appRank, bias)
    elif cate in cates:
        searchUpdate(soup, 'applist', cate, appRank, bias)
        if bias == 0:
            # substract length of category hot applist
            bias -= len(soup(class_='applist')[0]('li'))
        bias = bias + len(appRank)
    return bias, appRank


def updateAppRank(names, appRank, cate, bias):
    for i in range(len(names)):
        key = names[i]
        appRank.append([key, cate, bias+i+1])


def getNameList(items):
    names = [item('h5')[0].text.encode('u8') for item in items]
    return names

        
def searchUpdate(soup, classname, cate, appRank, bias):
    if cate == 'home':
        items = soup(class_=classname)[0]('li')
        names = getNameList(items) 
        updateAppRank(names, appRank, cate, bias)
    else:
        if bias == 0:
            # for category hot applist
            items = soup(class_=classname)[0]('li')
            names = getNameList(items) 
            updateAppRank(names, appRank, cate+'_hot', bias)
        # for category all applist
        items = soup(class_=classname)[1]('li')
        names = getNameList(items) 
        updateAppRank(names, appRank, cate, bias)

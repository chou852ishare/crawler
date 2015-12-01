# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['zhanzhengcelue', 'dongzuoqiangzhan', 'saichetiyu',
         'wangyouRPG', 'qipaizhuoyou', 'gedoukuaida', 
         'ertongyizhi', 'xiuxianchuangyi', 'feixingkongzhan',
         'paokuchuangguan', 'tafangmigong', 'monijingying']

def extract(page, cate, bias):
    apprank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        search_and_update(soup, 'applist', 'home', apprank, bias)
    elif cate in cates:
        search_and_update(soup, 'applist', cate, apprank, bias)
        if bias == 0:
            # substract length of category hot applist
            bias -= len(soup(class_='applist')[0]('li'))
        bias = bias + len(apprank)
    return bias, apprank


def update_apprank(names, apprank, cate, bias):
    for i in range(len(names)):
        key = names[i]
        apprank.append([key, cate, bias+i+1])


def get_name_list(items):
    names = [item('h5')[0].text.encode('u8') for item in items]
    return names

        
def search_and_update(soup, classname, cate, apprank, bias):
    if cate == 'home':
        items = soup(class_=classname)[0]('li')
        names = get_name_list(items) 
        update_apprank(names, apprank, cate, bias)
    else:
        # for category hot applist
        if bias == 0:
            items = soup(class_=classname)[0]('li')
            names = get_name_list(items) 
            update_apprank(names, apprank, cate+'_hot', bias)
        # for category all applist
        items = soup(class_=classname)[1]('li')
        names = get_name_list(items) 
        update_apprank(names, apprank, cate, bias)

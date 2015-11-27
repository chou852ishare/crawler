# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['xiuxianshijian', 'paokujingsu', 'dongzuosheji',   \
         'pukeqipai', 'tiyugedou', 'juesebanyan',           \
         'baoshixiaochu', 'wangluoyouxi', 'ertongyizhi',    \
         'tafangshouwei', 'jingyingcelue']

def extract(page, cate, bias):
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        searchUpdate(soup, 'j-top-list', 'home', appRank, bias)
    elif cate in cates:
        searchUpdate(soup, 'j-tag-list', cate, appRank, bias)
    return bias, appRank


def updateAppRank(names, pkgs, appRank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        appRank.append([key, cate, bias+i+1])


def getNameList(items, cate):
    names = [item(class_='app-desc')[0](class_='name')[0].text.encode('u8') for item in items]
    pkgs  = [item.attrs['data-pn'] for item in items]    
    return names, pkgs

        
def searchUpdate(soup, idname, cate, appRank, bias):
    items = soup(id=idname)[0]('li')
    names, pkgs = getNameList(items, cate) 
    updateAppRank(names, pkgs, appRank, cate, bias)

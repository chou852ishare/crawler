# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['xiuxianyizhi', 'wangluoyouxi', 'dongzuomaoxian',
         'qipaizhongxin', 'feixingsheji', 'jingyingcelue',
         'juesebanyan', 'tiyujingsu']

def extract(page, cate, bias):
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        searchUpdate(soup, 'app-list clearfix', 'home', appRank, bias)
    elif cate in cates:
        searchUpdate(soup, 'app-list clearfix', cate, appRank, bias)
    return bias, appRank


def updateAppRank(names, pkgs, appRank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        appRank.append([key, cate, bias+i+1])


def getNameList(items):
    names = [item(class_='com-install-btn')[0].attrs['appname'].encode('u8') for item in items]
    pkgs  = [item(class_='com-install-btn')[0].attrs['apk'] for item in items]
    return names, pkgs

        
def searchUpdate(soup, classname, cate, appRank, bias):
    items = soup(class_=classname)[0]('li')
    names, pkgs = getNameList(items) 
    updateAppRank(names, pkgs, appRank, cate, bias)

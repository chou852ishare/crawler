# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = {'juesebanyan'  :101587, 
        'xiuxianyizhi'  :19,     
        'dongzuomaoxian':20,     
        'wangluoyouxi'  :100451, 
        'tiyujingsu'    :51,     
        'feixingsheji'  :52,     
        'jingyingcelue' :53,     
        'qipaitiandi'   :54,     
        'ertongyouxi'   :102238}

def extract(page, cate, bias):
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        for c in cates:
            # for home category
            if c == 'ertongyouxi': continue
            searchUpdate(soup, 'srank', cates[c], 'home_'+c, appRank, bias)
        
        tops = {'topdownload': 'top_d', 'updownload': 'up_d'}
        for c in tops: 
            # for home top download and up download apps
            searchUpdate(soup, 'rankcon', tops[c], 'home_'+c, appRank, bias)
        
        rate = {'highrate': 'pjzg'}
        for c in rate:
            # for home high rate apps
            searchUpdate(soup, 'srank', rate[c], 'home_'+c, appRank, bias)
    
    elif cate in cates:
        searchUpdate(soup, 'iconList', 'iconList', cate, appRank, bias)
        bias = bias + len(appRank)
    return bias, appRank


def updateAppRank(names, pkgs, appRank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        appRank.append([key, cate, bias+i+1])


def getNameList(items, cate):
    if 'home' in cate:
        names = [item(class_='sname')[0].attrs['title'].encode('u8') for item in items]
        pkgs  = [item('a')[-1].attrs['href'].split('/')[-1].split('_')[-2] for item in items]
    else:
        names = [item('h3')[0].text.encode('u8') for item in items]
        pkgs  = [item('a')[-1].attrs['href'].split('/')[-1] for item in items]
    return names, pkgs

        
def searchUpdate(soup, classname, idn, cate, appRank, bias):
    if 'home' in cate:
        items = soup(class_=classname, cid=idn)[0]('li')
    else: 
        items = soup(class_=classname, id=idn)[0]('li')
    names, pkgs = getNameList(items, cate) 
    updateAppRank(names, pkgs, appRank, cate, bias)

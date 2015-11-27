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
    apprank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        for c in cates:
            # for home category
            if c == 'ertongyouxi': continue
            search_and_update(soup, 'srank', cates[c], 'home_'+c, apprank, bias)
        tops = {'topdownload': 'top_d', 'updownload': 'up_d'}
        for c in tops: 
            # for home top download and up download apps
            search_and_update(soup, 'rankcon', tops[c], 'home_'+c, apprank, bias)
        rate = {'highrate': 'pjzg'}
        for c in rate:
            # for home high rate apps
            search_and_update(soup, 'srank', rate[c], 'home_'+c, apprank, bias)
    elif cate in cates:
        search_and_update(soup, 'iconList', 'iconList', cate, apprank, bias)
        bias = bias + len(apprank)
    return bias, apprank


def update_apprank(names, pkgs, apprank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        apprank.append([key, cate, bias+i+1])


def get_name_list(items, cate):
    if 'home' in cate:
        names = [item(class_='sname')[0].attrs['title'].encode('u8') for item in items]
        pkgs  = [item('a')[-1].attrs['href'].split('/')[-1].split('_')[-2] for item in items]
    else:
        names = [item('h3')[0].text.encode('u8') for item in items]
        pkgs  = [item('a')[-1].attrs['href'].split('/')[-1] for item in items]
    return names, pkgs

        
def search_and_update(soup, classname, idn, cate, apprank, bias):
    if 'home' in cate:
        items = soup(class_=classname, cid=idn)[0]('li')
    else: 
        items = soup(class_=classname, id=idn)[0]('li')
    names, pkgs = get_name_list(items, cate) 
    update_apprank(names, pkgs, apprank, cate, bias)

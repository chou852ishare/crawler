# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['xiuxianyizhi', 'wangluoyouxi', 'dongzuomaoxian',
         'qipaizhongxin', 'feixingsheji', 'jingyingcelue',
         'juesebanyan', 'tiyujingsu']

def extract(page, cate, bias):
    apprank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        search_and_update(soup, 'app-list clearfix', 'home', apprank, bias)
    elif cate in cates:
        search_and_update(soup, 'app-list clearfix', cate, apprank, bias)
    return bias, apprank


def update_apprank(names, pkgs, apprank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        apprank.append([key, cate, bias+i+1])


def get_name_list(items):
    names = [item(class_='com-install-btn')[0].attrs['appname'].encode('u8') for item in items]
    pkgs  = [item(class_='com-install-btn')[0].attrs['apk'] for item in items]
    return names, pkgs

        
def search_and_update(soup, classname, cate, apprank, bias):
    items = soup(class_=classname)[0]('li')
    names, pkgs = get_name_list(items) 
    update_apprank(names, pkgs, apprank, cate, bias)

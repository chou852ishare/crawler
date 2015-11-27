# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['xiuxianshijian', 'paokujingsu', 'dongzuosheji',   
         'pukeqipai', 'tiyugedou', 'juesebanyan',           
         'baoshixiaochu', 'wangluoyouxi', 'ertongyizhi',    
         'tafangshouwei', 'jingyingcelue']

def extract(page, cate, bias):
    apprank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        search_and_update(soup, 'j-top-list', 'home', apprank, bias)
    elif cate in cates:
        search_and_update(soup, 'j-tag-list', cate, apprank, bias)
    return bias, apprank


def update_apprank(names, pkgs, apprank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        apprank.append([key, cate, bias+i+1])


def get_name_list(items, cate):
    names = [item(class_='app-desc')[0](class_='name')[0].text.encode('u8') for item in items]
    pkgs  = [item.attrs['data-pn'] for item in items]    
    return names, pkgs

        
def search_and_update(soup, idname, cate, apprank, bias):
    items = soup(id=idname)[0]('li')
    names, pkgs = get_name_list(items, cate) 
    update_apprank(names, pkgs, apprank, cate, bias)

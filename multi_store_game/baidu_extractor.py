# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['xiuxianyizhi', 'dongzuosheji', 
        'tiyujingji', 'jingyingyangcheng', 'juesebanyan', 
        'saichejingsu', 'monifuzhu', 'qipaizhuoyou']

def extract(page, cate, bias):
    apprank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        # recommendation apps
        search_and_update(soup, 'yui3-g sec-rec clearfix', 'home_rec', apprank, bias)
        # top hot apps
        search_and_update(soup, 'sec-hot tophot', 'home_tophot', apprank, bias)
        # must have apps
        search_and_update(soup, 'must', 'home_must', apprank, bias)
        # hot apps
        search_and_update(soup, 'sec-hot', 'home_hot', apprank, bias)
        # category reccomendation apps
        search_and_update(soup, 'sec-caterec', 'home_caterec', apprank, bias)
    elif cate in cates:
        search_and_update(soup, 'list-bd app-bd', cate, apprank, bias)
        bias = bias + len(apprank)
    return bias, apprank


def update_apprank(names, pkgs, apprank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        apprank.append([key, cate, bias+i+1])


def get_name_list(items, cate):
    if cate in ['home_must'] or cate in cates:
        names = [item(class_='name')[0].text.encode('u8') for item in items]
        pkgs  = [item(class_='inst-btn inst-btn-small quickdown')[0].attrs['data_package'] \
                for item in items]
    elif cate in ['home_caterec']:
        names = [item(class_='name')[0].text.encode('u8') \
                for item in items \
                if not (item.parent.has_attr('class') \
                and item.parent['class'][0] == 'cate-name')]
        pkgs  = [item(class_='inst-btn inst-btn-small quickdown')[0].attrs['data_package'] 
                for item in items \
                if not (item.parent.has_attr('class') 
                and item.parent['class'][0] == 'cate-name')]
    else:
        names = [item(class_='name')[0].text.encode('u8') for item in items]
        pkgs  = [item(class_='inst-btn-big quickdown')[0].attrs['data_package'] \
                for item in items]
    return names, pkgs

        
def search_and_update(soup, classname, cate, apprank, bias):
    if classname == 'sec-hot':
        items = soup(class_=classname)[1]('li')
    else:
        items = soup(class_=classname)[0]('li')
    names, pkgs = get_name_list(items, cate) 
    update_apprank(names, pkgs, apprank, cate, bias)

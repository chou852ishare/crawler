# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

cates = ['juesebanyan', 'xiuxianyizhi', 'dongzuomaoxian', 
         'wangluoyouxi', 'tiyujingsu', 'feixingsheji',
         'jingyingcelue','qipaitiandi', 'ertongyouxi']
    cate = {101587: 'juesebanyan',
            19:     'xiuxianyizhi',
            20:     'dongzuomaoxian',
            100451: 'wangluoyouxi',
            51:     'tiyujingsu',
            52:     'feixingsheji',
            53:     'jingyingcelue',
            54:     'qipaitiandi',
            102238: 'ertongyouxi'}

def extract(page, cate, bias):
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        # home juesebanyan
        searchUpdate(soup, '19', 'home_juesebanyan', appRank, bias)
        # home xiuxianyizhi
        searchUpdate(soup, 'sec-hot tophot', 'home_tophot', appRank, bias)
        # must have apps
        searchUpdate(soup, 'must', 'home_must', appRank, bias)
        # hot apps
        searchUpdate(soup, 'sec-hot', 'home_hot', appRank, bias)
        # category reccomendation apps
        searchUpdate(soup, 'sec-caterec', 'home_caterec', appRank, bias)
    elif cate in cates:
        searchUpdate(soup, 'list-bd app-bd', cate, appRank, bias)
        bias = bias + len(appRank)
    return bias, appRank


def updateAppRank(names, pkgs, appRank, cate, bias):
    for i in range(len(names)):
        #key = names[i] + '_' + pkgs[i]
        key = names[i]
        appRank.append([key, cate, bias+i+1])


def getNameList(items, cate):
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

        
def searchUpdate(soup, classname, cate, appRank, bias):
    if classname == 'sec-hot':
        items = soup(class_=classname)[1]('li')
    else:
        items = soup(class_=classname)[0]('li')
    names, pkgs = getNameList(items, cate) 
    updateAppRank(names, pkgs, appRank, cate, bias)

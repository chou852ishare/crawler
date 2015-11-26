# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

def extract(page, cate, bias):
    bias = 19
    appRank = [] 
    soup = BeautifulSoup(page)
    if cate == 'allranking':
        # recommendation apps
        recmd = soup(class_='yui3-g sec-rec clearfix')[0]
        items = recmd(class_='firrow')
        names = [item(class_='name')[0].text.encode('u8') for item in items]
        pkgs  = [item(class_='inst-btn-big quickdown')[0].attrs['data_package'] for item in items]
        # top hot apps
        recmd = soup(class_='sec-hot tophot')[0]
        items = recmd(class_='firrow')
        names = [item(class_='name')[0].text.encode('u8') for item in items]
        pkgs  = [item(class_='inst-btn-big quickdown')[0].attrs['data_package'] for item in items]
        
    
    for i in range(len(items)):
        key = names[i] + '_' + pkgs[i]
        appRank.append([key, 'home_rec', i+1])
    return bias, appRank

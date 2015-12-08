# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import traceback
from bs4 import BeautifulSoup
from selenium import webdriver

prefix = 'http://product.cnmo.com/pro_sub_manu/sub_57_manu_1763_1_%s.shtml'
output = './output/'

def get_soup(url):
    src  = urllib2.urlopen(url, timeout=3)
    page = src.read()
    soup = BeautifulSoup(page)
    return soup


def crawl_page(page):
    url = prefix % page
    try:
        soup = get_soup(url)
        itms = soup(class_='btn', id='comparePicList')
        pars = [item('a')[1]['href'] for item in itms]
        for k,purl in enumerate(pars):
            print page, k, purl
            psoup = get_soup(purl)
            fname = output + ('lenovo_%s_%s' % (page, k)) + psoup(class_='clearfix modle_title')[0]('h1')[0].text.encode('u8')
            print >> open(fname, 'w'), psoup
    except Exception, e:
        print fname
        traceback.print_exc()


def main():
    for page in range(1,15):
        crawl_page(page)


if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

tagsys = {}

def run():
    url = 'http://www.contentharmony.com/blog/facebook-ad-targeting/'
    soup = get_soup(url)
    targets = soup(class_='slant-header')
    for target in targets:
        title = target.text.encode('u8').strip()
        if title.split(' ')[-1] == 'Targeting':
            print title 
   

def get_soup(url):
    src = urllib2.urlopen(url, timeout=5)
    page = src.read()
    soup = BeautifulSoup(page)
    return soup


def main():
    run()


if __name__ == '__main__':
    main()

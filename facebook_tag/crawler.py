# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from bs4 import BeautifulSoup

tagsys = {}
tag = {}
tagfile = './tag.lsv'

def run():
    open(tagfile, 'w').close()
    url = 'http://www.contentharmony.com/blog/facebook-ad-targeting/'
    soup = get_soup(url)
    targets = soup(class_='slant-header')
    for target in targets:
        title = target.text.encode('u8').strip()
        if title.split(' ')[-1] == 'Targeting':
            tag.clear()
            content = find_content(target)
            outline = ''
            if content(class_='twocol-one'):
                for col in content(class_='twocol-one'):
                    find_childrentwocol(col, title, tag, outline)
            if content(class_='threecol-one'):
                for col in content(class_='threecol-one'):
                    find_childrenthreecol(col, title, tag, outline)
            else:
                find_childrencol(content, title, tag, outline)


def find_childrencol(col, key, tag, outline):
    if col('ul'):
        ul1 = col('ul')[0]
        find_childrenul(ul1, key, tag, outline)
        for ul in ul1.findNextSiblings():
            if not ul('li'): continue
            find_childrenul(ul, key, tag, outline)
    

def find_childrentwocol(col, key, tag, outline):
    outline = key + '|'
    if col('h3'):
        subkey = col('h3')[0].text.encode('u8').strip()
    else:
        return
    if tag.has_key(key):
        tag[key][subkey] = {}
    else:
        tag[key] = {subkey: {}}
    if col('ul'):
        ul1 = col('ul')[0]
        find_childrenul(ul1, subkey, tag, outline)
        for ul in ul1.findNextSiblings():
            if not ul('li'): continue
            find_childrenul(ul, subkey, tag, outline)


def find_childrenthreecol(col, key, tag, outline):
    outline = key + '|'
    if col('strong'):
        subkey = col('strong')[0].text.encode('u8').strip()
    else:
        return
    if tag.has_key(key):
        tag[key][subkey] = {}
    else:
        tag[key] = {subkey: {}}
    if col('ul'):
        ul1 = col('ul')[0]
        find_childrenul(ul1, subkey, tag, outline)
        for ul in ul1.findNextSiblings():
            if not ul('li'): continue
            find_childrenul(ul, subkey, tag, outline)


def find_childrenul(parentul, key, tag, outline):
    li1 = parentul('li')[0]
    recurfind_childrenli(li1, key, tag, outline)
    for li in li1.findNextSiblings():
        recurfind_childrenli(li, key, tag, outline)


def recurfind_childrenli(parentli, key, tag, outline):
    outline += demess(key) + '|'
    if not parentli('ul'):
        if tag.has_key(key):
            tag[key][parentli.text.strip()] = {}
        else:
            tag[key] = {parentli.text.strip(): {}}
        outline += demess(parentli.text.strip().encode('u8')) + '|'
        with open(tagfile, 'a') as f:
            print >> f, outline
        return
    elif parentli('strong'):
        subkey = parentli('strong')[0].text.strip().encode('u8')
    else:
        subkey = str(parentli).decode('u8', 'ignore').split('<ul>')[0].strip().replace('<li>','').encode('u8')
    li1 = parentli('ul')[0]('li')[0]
    tag[key] = {}
    recurfind_childrenli(li1, subkey, tag[key], outline)
    for li in li1.findNextSiblings():
        recurfind_childrenli(li, subkey, tag[key], outline)


def demess(s):
    return s.strip().replace('|', '')


def find_content(target):
    content = '' 
    for s in target.find_next_siblings():
        if s.has_attr('class') and 'slant-header' in s['class']: break
        content += str(s)
    return BeautifulSoup(content, 'lxml')


def get_soup(url):
    src = urllib2.urlopen(url, timeout=5)
    page = src.read()
    soup = BeautifulSoup(page, 'lxml')
    return soup


def main():
    run()


if __name__ == '__main__':
    main()

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from bs4 import BeautifulSoup

tagsys = {}
tag = {}

def find_childrentwocol(col, key, tag, outline):
    outline += key + '|'
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
        print outline
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


def main():
    col = BeautifulSoup(open('financial.html').read(), "lxml")
    ul0 = col('ul')[0]
    li0 = col('ul')[0]('li')[0]
    tag = {}
    outline = ''
    find_childrentwocol(col, 'Demographic', tag, outline)


if __name__ == '__main__':
    main()

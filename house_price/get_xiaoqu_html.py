# -*- coding: utf-8 -*-

import urllib2
import re
from multiprocessing import Pool
from csv import DictReader
from bs4 import BeautifulSoup

def get_citylist(filename):
    f = open(filename, 'r')
    dreader = DictReader(f)
    citylist = []
    for row in dreader:
        citylist.append(row['city_abbrev'])
    return citylist

def get_sub_xiaoquhtml(citylist, k, K):
    # divide cities into K set
    # process k-th set
    alphs = 'ABCDEFG' +\
            'HIJKLMN' +\
            'OPQRST'  +\
            'UVWXYZ'
    step = len(citylist) / K
    for city in citylist[k::step]:
        for alph in alphs:
            try:
                f = open('./xiaoqu_list/xiaoqulist_%s_%s' % (city, alph), 'r')
            except:
                continue
            lines = f.readlines()
            for line in lines[1:]:
                site = line.split(',')[1]
                if len(site) < 1: continue
                xiaoqu = re.search(r'http://(.*)\.fang\.com', site).group(1)
                src  = urllib2.urlopen(site, timeout=5)
                page = src.read()
                soup = BeautifulSoup(page)
                info = soup(class_='leftinfo')[0]
                print city, xiaoqu
                print info(class_='pred pirceinfo')[0].text


def run():
    citylist = get_citylist('citylist')
    # multiprocessing
    nproc = 16
    p = Pool(nproc)
    for k in range(nproc):
        p.apply_async(get_sub_xiaoquhtml, args=(citylist,k,nproc)) 
    p.close()
    p.join()


if __name__ == '__main__':
    run()


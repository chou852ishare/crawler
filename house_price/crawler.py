# -*- coding: utf-8 -*-

import re
import urllib2
from bs4 import BeautifulSoup

def format_citylist(infile, outfile):
    fi = open(infile, 'r')
    fo = open(outfile, 'w')
    print >> fo, 'city_abbrev,city,province'
    lines = fi.readlines()
    for line in lines:
        mp = re.search(r'<td valign=\"top\"><strong>(.*)</strong></td>', line)
        mc = re.search(r'<a href=\"http://(.*).fang.com/\" target=\"_blank\"(.*)>(.*)</a>', line)
        if mp and len(mp.groups()) > 0 and ('&' not in mp.group(1)):
            province = mp.group(1)
        if mc and len(mc.groups()) > 1:
            abbr = mc.group(1)
            city = mc.group(3)
            print >> fo, abbr + ',' + city + ',' + province
    fi.close()
    fo.close()


def get_xiaoqulist(infile, outfile):
    fi  = open(infile, 'r')
    log = open('xiaoqu.log', 'w')
    lines = fi.readlines()
    for line in lines[1:]:
        abbr = line.split(',')[0].encode('utf8')
        city = line.split(',')[1].decode('gbk').encode('utf8')
        fo   = open(outfile+'_'+abbr, 'w')
        print >> fo, 'xiaoqu_en,xiaoqu_cn,city_abbrev,city,province'
        alph = 'ABCDEFG' + \
               'HIJKLMN' + \
               'OPQRST' + \
               'UVWXYZ'
        for x in alph:
            try:
                src  = urllib2.urlopen('http://esf.%s.fang.com/housing/xiaoqu_%s.htm' % (abbr, x), timeout = 5)
                page = src.read().decode('gbk')
                soup = BeautifulSoup(page)
                guide = soup(class_='guide')[0].encode('utf8')
                if city not in guide:
                    continue
                xiaoqu = soup(class_='busHsIndex')[0].find_all('a')
                for xq in xiaoqu:
                    vill = xq.text.encode('utf8').strip()
                    href = xq['href']
                    try:
                        site = get_site(abbr, vill, href) 
                        if site == '':
                            print >> log, '%s,%s,%s,%s,%s,%s' % (abbr, city, x, vill, href, 'null_xiaoqu')
                        else:
                            print >> fo, vill + ',' + site
                    except:
                        print >> log, '%s,%s,%s,%s,%s,%s' % (abbr, city, x, vill, href, 'fail_xiaoqu')
            except:
                print >> log, '%s,%s,%s,%s' % (abbr, city, x, 'null')
        fo.close()
    fi.close()
    log.close()


def get_site(abbr, vill, href):
    src1 = urllib2.urlopen('http://esf.%s.fang.com%s' % (abbr, href), timeout=5)
    page = src1.read()
    soup = BeautifulSoup(page)
    hous = soup(class_='village mt10')[0]
    vila = hous(class_='hTitle')[0].a.text.encode('utf8')
    site = ''
    if vill == vila:
        site = hous(class_='iconXQ ml10')[0]['href']
    return site
    


if __name__ == '__main__':
    cityhtml   = 'citylist_html'
    citylist   = 'citylist'
    xiaoqulist = 'xiaoqulist'
    format_citylist(cityhtml, citylist)
    get_xiaoqulist(citylist, xiaoqulist)
    

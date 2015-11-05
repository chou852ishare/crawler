import re
import urllib2

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
    fi = open(infile, 'r')
    fo = open(outfile, 'w')
    print >> fo, 'xiaoqu_en,xiaoqu_cn,city_abbrev,city,province'
    lines = fi.readlines()
    for line in lines:
        abbr = line.split(',')[0]
        alph = 'A'
        print 'esf.%s.fang.com/housing/xiaoqu_%s.htm' % (abbr, alph)

if __name__ == '__main__':
    cityhtml   = 'citylist_html'
    citylist   = 'citylist'
    xiaoqulist = 'xiaoqulist'
    format_citylist(cityhtml, citylist)
    get_xiaoqulist(citylist, xiaoqulist)
    

import urllib2
from datetime import datetime

def get_allrank():
    try:
        url  = 'http://zhushou.360.cn/list/hotList/cid/2'
        src  = urllib2.urlopen(url, timeout=5)
        page = src.read()
        dt   = datetime.now().strftime('%Y%m%d_%H%M%S')
        fn   = './html/allranking_%s.html' % dt
        f    = open(fn, 'w')
        print >> f, page
    except:
        log  = open('./zhushou360.log', 'a')
        print >> log, 'allrank fail'
        log.close()


def get_categoryrank():
    pref = 'http://zhushou.360.cn/list/index/cid/%s/?page=%s' 
    cate = {101587: 'juesebanyan',
            19:     'xiuxianyizhi',
            20:     'dongzuomaoxian',
            100451: 'wangluoyouxi',
            51:     'tiyujingsu',
            52:     'feixingsheji',
            53:     'jingyingcelue',
            54:     'qipaitiandi',
            102238: 'ertongyouxi'}
    log = open('zhushou360.log', 'a')
    for cid in cate.keys():
        c = cate[cid]
        for p in range(1,51):
            try:
                url  = pref % (cid, p)
                src  = urllib2.urlopen(url, timeout=5)
                page = src.read()
                dt   = datetime.now().strftime('%Y%m%d_%H%M%S')
                f    = open('./html/%s_%s_%s.html' % (c,p,dt), 'w')
                print >> f, page
                f.close()
            except:
                print >> log, dt, c, p, 'fail'
                continue
    log.close()



if __name__ == '__main__':
    get_allrank()
    get_categoryrank()

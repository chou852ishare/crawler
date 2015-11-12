import urllib2
from datetime import datetime

def get_all_rank():
    try:
        site = 'http://shouji.baidu.com/game'
        dt   = datetime.now().strftime('%Y%m%d_%H%M%S')
        fn   = './html/allranking_%s.html' % dt
        src  = urllib2.urlopen(site, timeout=5)
        page = src.read()
        f    = open(fn, 'w')
        print >> f, page
        f.close()
    except:
        log = open('baidu.log', 'a')
        print >> log, dt, 'allrank fail'
        log.close()

def get_category_rank():
    pref = 'http://shouji.baidu.com/game/list?cid=%s&page_num=%s' 
    cate = {1: 'xiuxianyizhi',
            3: 'dongzuosheji',
            5: 'tiyujingji',
            8: 'jingyingyangcheng',
            2: 'juesebanyan',
            6: 'saichejingsu',
            4: 'monifuzhu',
            7: 'qipaizhuoyou'}
    log = open('baidu.log', 'a')
    for cid in cate.keys():
        c = cate[cid]
        for p in range(1,9):
            dt = datetime.now().strftime('%Y%m%d_%H%M%S')
            f  = open('./html/%s_%s_%s.html' % (c,p,dt), 'w')
            url = pref % (cid, p)
            try:
                src  = urllib2.urlopen(url, timeout=5)
                page = src.read()
                print >> f, page
                f.close()
            except:
                print >> log, dt, c, p, 'fail'
                continue
    log.close()


if __name__ == '__main__':
    get_all_rank()
    get_category_rank()

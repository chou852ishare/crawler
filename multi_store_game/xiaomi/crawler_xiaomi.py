import urllib2
from datetime import datetime

def get_allrank():
    try:
        url  = 'http://app.mi.com/gTopList'
        src  = urllib2.urlopen(url, timeout=5)
        page = src.read()
        dt   = datetime.now().strftime('%Y%m%d_%H%M%S')
        fn   = './html/allranking_%s.html' % dt
        f    = open(fn, 'w')
        print >> f, page
    except:
        log  = open('./xiaomi.log', 'a')
        print >> log, 'allrank fail'
        log.close()


def get_categoryrank():
    pref = 'http://app.mi.com/category/%s#page=%s' 
    cate = {16: 'zhanzhengcelue',
            17: 'dongzuoqiangzhan',
            18: 'saichetiyu',
            19: 'wangyouRPG',
            20: 'qipaizhuoyou',
            21: 'gedoukuaida',
            22: 'ertongyizhi',
            23: 'xiuxianchuangyi',
            25: 'feixingkongzhan',
            26: 'paokuchuangguan',
            28: 'tafangmigong',
            29: 'monijingying',}
    log = open('xiaomi.log', 'a')
    for cid in cate.keys():
        c = cate[cid]
        for p in range(50):
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

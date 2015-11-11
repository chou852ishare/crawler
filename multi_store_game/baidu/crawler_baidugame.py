import urllib2

def get_all_rank():
    site = 'http://shouji.baidu.com/game'
    fn   = './html/all_ranking.html'
    src  = urllib2.urlopen(site, timeout=5)
    page = src.read()
    f    = open(fn, 'w')
    print >> f, page
    f.close()

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
    log = open('baidu.log', 'w')
    for cid in cate.keys():
        c = cate[cid]
        for p in range(1,9):
            f = open('%s_%s.html' % (c,p), 'w')
            url = pref % (i, p)
            try:
                src  = urllib2.urlopen(url, timeout=5)
                page = src.read()
                print >> f, page
                f.close()
            except:
                print >> log, c, p, 'fail'
                continue
    log.close()


if __name__ == '__main__':
    get_all_rank()
    get_category_rank()

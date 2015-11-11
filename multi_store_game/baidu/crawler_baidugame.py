import urllib2

def get_all_rank():
    site = 'http://shouji.baidu.com/game'
    fn   = './html/all_ranking.html'
    src  = urllib2.urlopen(site, timeout=5)
    page = src.read()
    f    = open(fn, 'w')
    print >> f, page
    f.close()

def get_xiuxianyizhi_rank():
    for i in range(1,9):
        site = 'http://shouji.baidu.com/game/list?cid=401&page_num=%s' % i

if __name__ == '__main__':
    get_all_rank()
    get_xiuxianyizhi_rank()

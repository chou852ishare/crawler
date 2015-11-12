# -*- coding: utf-8 -*-
from selenium import webdriver
from datetime import datetime

def get_allrank():
    driver = webdriver.PhantomJS('phantomjs')
    try:
        driver.get('http://sj.qq.com/myapp/category.htm?orgame=2')
        loadmore = u'加载更多'
        count = 0
        while loadmore == u'加载更多' and count < 10:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            loadmore = driver.find_element_by_class_name('load-more-btn').text
            count += 1
        dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        fn = './html/allranking_%s.html' % dt
        f  = open(fn, 'w')
        print >> f, driver.page_source.encode('utf8')
        f.close()
    except:
        log = open('./yingyongbao.log', 'a')
        print >> log, 'allrank fail'
        log.close()
    driver.quit()


def get_categoryrank():
    pref = 'http://sj.qq.com/myapp/category.htm?orgame=2&categoryId=%s'
    cate = {147: 'xiuxianyizhi',
            121: 'wangluoyouxi',
            144: 'dongzuomaoxian',
            148: 'qipaizhongxin',
            149: 'feixingsheji',
            153: 'jingyingcelue',
            146: 'juesebanyan',
            151: 'tiyujingsu',}
    log = open('yingyongbao.log', 'a')
    for cid in cate.keys():
        c = cate[cid]
        driver = webdriver.PhantomJS('phantomjs')
        try:
            url = pref % cid
            driver.get(url)
            loadmore = u'加载更多'
            count = 0
            while loadmore == u'加载更多' and count < 10:
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                loadmore = driver.find_element_by_class_name('load-more-btn').text
                count += 1
            dt = datetime.now().strftime('%Y%m%d_%H%M%S')
            f  = open('./html/%s_%s.html' % (c,dt), 'w')
            print >> f, driver.page_source.encode('utf8')
            f.close()
        except:
            print >> log, dt, c, 'fail'
        driver.quit()
    log.close()


if __name__ == '__main__':
    get_allrank()
    get_categoryrank()

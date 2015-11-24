# -*- coding: utf-8 -*-
from selenium import webdriver
from datetime import datetime
import time
import urllib

def get_allrank():
    driver = webdriver.Firefox()
    try:
        driver.get('http://www.wandoujia.com/top/game')
        loadmore = u'查看更多'
        count = 0
        while loadmore == u'查看更多' and count < 50:
            btnmore = driver.find_element_by_id('j-refresh-btn')
            btnmore.click()
            time.sleep(2)
            loadmore = btnmore.text
            count += 1
        dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        fn = './html/allranking_%s.html' % dt
        f  = open(fn, 'w')
        print >> f, driver.find_element_by_class_name('container').get_attribute('innerHTML').encode('utf8')
        f.close()
    except:
        log = open('./wandoujia.log', 'a')
        print >> log, 'allrank fail'
        log.close()
    driver.quit()


def get_categoryrank():
    pref = 'http://www.wandoujia.com/tag/%s'
    cate = {'休闲时间': 'xiuxianshijian',
            '跑酷竞速': 'paokujingsu',
            '动作射击': 'dongzuosheji',
            '扑克棋牌': 'pukeqipai',
            '体育格斗': 'tiyugedou',
            '角色扮演': 'juesebanyan',
            '宝石消除': 'baoshixiaochu',
            '网络游戏': 'wangluoyouxi',
            '儿童益智': 'ertongyizhi',
            '塔防守卫': 'tafangshouwei',
            '经营策略': 'jingyingcelue',}
    log = open('wandoujia.log', 'a')
    driver = webdriver.Firefox()
    for cid in cate.keys():
        c = cate[cid]
        tag = urllib.quote(cid)
        try:
            dt  = datetime.now().strftime('%Y%m%d_%H%M%S')
            url = pref % tag
            driver.get(url)
            loadmore = u'查看更多'
            count = 0
            while loadmore == u'查看更多' and count < 50:
                btnmore = driver.find_element_by_id('j-refresh-btn')
                btnmore.click()
                time.sleep(2)
                loadmore = btnmore.text
                count += 1
            f = open('./html/%s_%s.html' % (c,dt), 'w')
            print >> f, driver.find_element_by_class_name('container').get_attribute('innerHTML').encode('utf8')
            f.close()
        except:
            print >> log, dt, c, 'fail'
    driver.quit()
    log.close()


if __name__ == '__main__':
    get_allrank()
    get_categoryrank()

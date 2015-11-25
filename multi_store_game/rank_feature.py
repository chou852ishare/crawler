# -*- coding: utf-8 -*-

import re
import glob
from bs4 import BeautifulSoup


storeCates= {'baidu':          ['allranking'], #'xiuxianyizhi', 'dongzuosheji', 'tiyujingji', 'jingyingyangcheng',
                                #'juesebanyan', 'saichejingsu', 'monifuzhu', 'qipaizhuoyou'],
             'wandoujia':      ['allranking', 'xiuxianshijian', 'paokujingsu', 'dongzuosheji', 'pukeqipai',
                                'tiyugedou', 'juesebanyan', 'baoshixiaochu', 'wangluoyouxi', 'ertongyizhi',
                                'tafangshouwei', 'jingyingcelue'],
             'xiaomi':         ['allranking', 'zhanzhengcelue', 'dongzuoqiangzhan', 'saichetiyu', 'wangyouRPG',
                                'qipaizhuoyou', 'gedoukuaida', 'ertongyizhi', 'xiuxianchuangyi', 'feixingkongzhan',
                                'paokuchuangguan', 'tafangmigong', 'monijingying'],
             'yingyongbao':    ['allranking', 'xiuxianyizhi', 'wangluoyouxi', 'dongzuomaoxian', 'qipaizhongxin',
                                'feixingsheji', 'jingyingcelue', 'juesebanyan', 'tiyujingsu'],
             'zhushou360Cats': ['allranking', 'juesebanyan', 'xiuxianyizhi', 'dongzuomaoxian', 'wangluoyouxi',
                                'tiyujingsu', 'feixingsheji','jingyingcelue','qipaitiandi', 'ertongyouxi']}


def queryThisStore(store, date):
    htmlPath = '/home/zzhou/crawler/multi_store_game/%s/html' % store
    if store not in storeCates:
        return Null
    cateList = storeCates[store]
    for cate in cateList:
        fList = glob.glob('%s/%s_*_%s*' % (htmlPath, cate, date))
        print cate, fList
        for bias,fn in enumerate(fList):
            with open(fn) as f:
                page = f.read()
                if store == 'baidu':
                    print store, date, cate, bias, fn
                    #baiduExtracter.extract(page, cate, bias)
                elif store == 'wandoujia':
                    #wandoujiaExtracter.extract(page, cate, bias)
                    pass
                elif store == 'xiaomi':
                    #xiaomiExtracter.extract(page, cate, bias)
                    pass
                elif store == 'xiaomi':
                    #yingyongbaoExtracter.extract(page, cate, bias)
                    pass
                elif store == 'xiaomi':
                    #zhushou360Extracter.extract(page, cate, bias)
                    pass
                else:
                    pass
    

def getRankFeature(date):
    storeList = ['baidu'] #, 'wandoujia', 'xiaomi', 'yingyongbao', 'zhushou360']
    for store in storeList:
        queryThisStore(store, date)


if __name__ == '__main__':
    date = '20151120'
    getRankFeature(date)

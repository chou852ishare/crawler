# -*- coding: utf-8 -*-

import re
import glob

import BaiduExtractor

rankDB = {}
storeCates= {'baidu': ['allranking', 'xiuxianyizhi', 'dongzuosheji',\
                'tiyujingji', 'jingyingyangcheng', 'juesebanyan', \
                'saichejingsu', 'monifuzhu', 'qipaizhuoyou'],
             'wandoujia': ['allranking', 'xiuxianshijian', 'paokujingsu', 'dongzuosheji', 'pukeqipai',
                                'tiyugedou', 'juesebanyan', 'baoshixiaochu', 'wangluoyouxi', 'ertongyizhi',
                                'tafangshouwei', 'jingyingcelue'],
             'xiaomi': ['allranking', 'zhanzhengcelue', 'dongzuoqiangzhan', 'saichetiyu', 'wangyouRPG',
                                'qipaizhuoyou', 'gedoukuaida', 'ertongyizhi', 'xiuxianchuangyi', 'feixingkongzhan',
                                'paokuchuangguan', 'tafangmigong', 'monijingying'],
             'yingyongbao': ['allranking', 'xiuxianyizhi', 'wangluoyouxi', 'dongzuomaoxian', 'qipaizhongxin',
                                'feixingsheji', 'jingyingcelue', 'juesebanyan', 'tiyujingsu'],
             'zhushou360Cats': ['allranking', 'juesebanyan', 'xiuxianyizhi', 'dongzuomaoxian', 'wangluoyouxi',
                                'tiyujingsu', 'feixingsheji','jingyingcelue','qipaitiandi', 'ertongyouxi']}


def getRankFeature(date):
    storeList = ['baidu'] #, 'wandoujia', 'xiaomi', 'yingyongbao', 'zhushou360']
    for store in storeList:
        queryThisStore(store, date)


def queryThisStore(store, date):
    if store == 'baidu':
        extract = BaiduExtractor.extract
    elif store == 'wandoujia':
        #extract = WandoujiaExtractor.extract
        pass
    elif store == 'xiaomi':
        #extract = XiaomiExtractor.extract
        pass
    elif store == 'yingyongbao':
        #extract = YingyongbaoExtractor.extract
        pass
    elif store == 'zhushou360':
        #extract = Zhushou360Extractor.extract
        pass
    else:
        return None
    #htmlPath = '/home/zzhou/crawler/multi_store_game/%s/html' % store
    htmlPath = '%s/html' % store
    if store not in storeCates:
        return None
    cateList = storeCates[store]
    # query app-rank dict
    # for each category (and each webpage of a category)
    for cate in cateList:
        fList = glob.glob('%s/%s*%s*' % (htmlPath, cate, date))
        bias = 0
        for fn in fList:
            with open(fn) as f:
                page = f.read()
                bias, appRank = extract(page, cate, bias)
                updateRankDB(appRank, store)


def updateRankDB(appRank, store):
    # appRank format: [app, cate, rank]
    # rankDB format: {app: {store: {cate: rank}}}
    for item in appRank:
        app  = item[0]
        cate = item[1]
        rank = item[2]
        if app not in rankDB:
            # w/o app
            rankDB[app] = {store: {cate: rank}}
        elif store not in rankDB[app]:
            # w/ app, w/o store
            rankDB[app][store] = {cate: rank}
        elif cate not in rankDB[app][store]:
            # w/ app and store, w/o cate
            rankDB[app][store][cate] = rank
        else:
            # w/ app and store and cate
            # data conflict, remain previous value
            continue
    # debug
    f = open('text', 'w')
    for app in rankDB:
        scr = rankDB[app]
        for store in scr:
            cr = scr[store]
            for cate in cr:
                rank = cr[cate]
                print >> f, app, '|', store, '|', cate, '|', rank


if __name__ == '__main__':
    date = '20151126'
    getRankFeature(date)

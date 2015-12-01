#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import glob

import baidu_extractor
import wandoujia_extractor
import xiaomi_extractor
import yingyongbao_extractor
import zhushou360_extractor

rankDB = {}
storecates= {'baidu': ['allranking', 'xiuxianyizhi', 'dongzuosheji',        
                       'tiyujingji', 'jingyingyangcheng', 'juesebanyan',           
                       'saichejingsu', 'monifuzhu', 'qipaizhuoyou'],
             'wandoujia': ['allranking', 'xiuxianshijian', 'paokujingsu',   
                       'dongzuosheji', 'pukeqipai', 'tiyugedou',                   
                       'juesebanyan', 'baoshixiaochu', 'wangluoyouxi',             
                       'ertongyizhi', 'tafangshouwei', 'jingyingcelue'],
             'xiaomi': ['allranking', 'zhanzhengcelue', 'dongzuoqiangzhan', 
                       'saichetiyu', 'wangyouRPG', 'qipaizhuoyou', 
                       'gedoukuaida', 'ertongyizhi', 'xiuxianchuangyi',
                       'feixingkongzhan', 'paokuchuangguan', 'tafangmigong', 
                       'monijingying'],
             'yingyongbao': ['allranking', 'xiuxianyizhi', 'wangluoyouxi', 
                       'dongzuomaoxian', 'qipaizhongxin', 'feixingsheji', 
                       'jingyingcelue', 'juesebanyan', 'tiyujingsu'],
             'zhushou360': ['allranking', 'juesebanyan', 'xiuxianyizhi', 
                       'dongzuomaoxian', 'wangluoyouxi', 'tiyujingsu', 
                       'feixingsheji','jingyingcelue','qipaitiandi', 
                       'ertongyouxi']}


def query_this_store(store, date):
    if store == 'baidu':
        extract = baidu_extractor.extract
    elif store == 'wandoujia':
        extract = wandoujia_extractor.extract
    elif store == 'xiaomi':
        extract = xiaomi_extractor.extract
    elif store == 'yingyongbao':
        extract = yingyongbao_extractor.extract
    elif store == 'zhushou360':
        extract = zhushou360_extractor.extract
    else:
        return None
    #htmlpath = '/home/zzhou/crawler/multi_store_game/%s/html' % store
    htmlpath = '%s/html' % store
    if store not in storecates:
        return None
    catelist = storecates[store]
    # query app-rank dict
    # for each category (and each webpage of a category)
    for cate in catelist:
        fnlist = glob.glob('%s/%s*%s*' % (htmlpath, cate, date))
        sort_by_page(fnlist, store)
        bias = 0
        for fn in fnlist:
            with open(fn) as f:
                page = f.read()
                bias, apprank = extract(page, cate, bias)
                update_rankDB(apprank, store)


def sort_by_page(fnlist, store):
    cmp_by_page = lambda x,y: cmp(int(x.split('_')[1]), int(y.split('_')[1]))
    if store in ['baidu', 'xiaomi', 'zhushou360']:
        fnlist.sort(cmp=cmp_by_page)


def update_rankDB(apprank, store):
    # apprank format: [app, cate, rank]
    # rankDB format: {app: {store: {cate: rank}}}
    for item in apprank:
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
    
    
def write_result(filename):
    f = open(filename, 'w')
    for app in rankDB:
        scr = rankDB[app]
        outline = app 
        for store in scr:
            cr = scr[store]
            outline += '|' + store + ' '
            for cate in cr:
                rank = cr[cate]
                outline += '%s:%s ' % (cate, rank)
        print >> f, outline


def get_features(date):
    for store in storecates:
        query_this_store(store, date)
    write_result('result')


if __name__ == '__main__':
    date = '20151127'
    get_features(date)

# !/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import traceback
from bs4 import BeautifulSoup

outpath = './output/*'
outfile = './lenovo_phone_info'
info = {}
keys = ['参考价格', '商家报价', '上市时间', 'CPU型号', '屏幕尺寸', '运行内存', '屏幕分辨率',
        '机身容量', '操作系统', '后置相机', '前置相机', '外观设计', 
        '运营商支持', '网络模式', 'SIM卡类型', 'WiFi', '蓝牙', 
        '外观设计', '手机颜色', '手机类型', '手机尺寸', '手机重量', 
        '电池类型', '电池更换', '通话时间', '待机时间', '屏幕尺寸', 
        '屏幕材质', '屏幕色数', '屏幕分辨率', '像素密度', '触控方式', 
        '屏幕特性', '操作系统', '用户界面', 'CPU型号', '核心数', 
        '主频', 'CPU制程', 'CPU架构', 'GPU型号', '运行内存', 
        '机身容量', '容量扩展', '传感器类型', '后置相机', '前置相机', 
        '闪光灯', '视频拍摄', '拍照特性', '视频格式', '音乐格式', 
        '音乐特性', '图片格式', '文档格式', 'GPS', '感应器', 
        'USB接口', '耳机接口', '无线连接', '日常功能', '键盘类型', 
        '输入方式', '输入法', '特殊功能', '网友还叫它']


def get_info(filename):
    f = open(filename)
    page = f.read()
    soup = BeautifulSoup(page)
    canshulist = soup(class_='canshu-list')
    # phone model
    try:
        model = soup(class_='clearfix modle_title')[0]('h1')[0].text.encode('u8')
        info['手机型号'] = demess(model)
    except:
        info['手机型号'] = ''
    # price
    try:
        price  = soup(class_='Bid-price')[0].text.encode('u8')
        dealer = soup(id='dealerPriceArea')[0].text.split('[')[0].encode('u8')
        info['参考价格'] = demess(price)
        info['商家报价'] = demess(dealer)
    except:
        info['参考价格'] = ''
        info['商家报价'] = ''
    # basic info
    try:
        basic = soup(class_='outline clearfix')[0]('li')
        for li in basic:
            lines = li.text.encode('u8').split('：')
            tagnm = demess(lines[0])
            value = demess(lines[1])
            info[tagnm] = value
    except:
        info['上市时间'] = ''
        info['CPU型号'] = ''
        info['屏幕尺寸'] = ''
        info['运行内存'] = ''
        info['屏幕分辨率'] = ''
        info['机身容量'] = ''
        info['操作系统'] = ''
        info['后置相机'] = ''
        info['前置相机'] = ''
        info['外观设计'] = ''
    # provider and network
    try:
        network = findcanshu(canshulist, 'typeName2')
        for li in network('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['运营商支持'] = ''
        info['网络模式'] = ''
        info['SIM卡类型'] = ''
        info['WiFi'] = ''
        info['蓝牙'] = ''
    # shape info
    try:
        shape = findcanshu(canshulist, 'typeName3')
        for li in shape('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['外观设计'] = ''
        info['手机颜色'] = ''
        info['手机类型'] = ''
        info['手机尺寸'] = ''
        info['手机重量'] = ''
        info['电池类型'] = ''
        info['电池更换'] = ''
        info['通话时间'] = ''
        info['待机时间'] = ''
    # screen info
    try:
        screen = findcanshu(canshulist, 'typeName5')
        for li in screen('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['屏幕尺寸'] = ''
        info['屏幕材质'] = ''
        info['屏幕色数'] = ''
        info['屏幕分辨率'] = ''
        info['像素密度'] = ''
        info['触控方式'] = ''
        info['屏幕特性'] = ''
    # os and hardware info
    try:
        oshw = findcanshu(canshulist, 'typeName17')
        for li in screen('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['操作系统'] = ''
        info['用户界面'] = ''
        info['CPU型号'] = ''
        info['核心数'] = ''
        info['主频'] = ''
        info['CPU制程'] = ''
        info['CPU架构'] = ''
        info['GPU型号'] = ''
        info['运行内存'] = ''
        info['机身容量'] = ''
        info['容量扩展'] = ''
    # camera 
    try:
        camera = findcanshu(canshulist, 'typeName7')
        for li in camera('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['传感器类型'] = ''
        info['后置相机'] = ''
        info['前置相机'] = ''
        info['闪光灯'] = ''
        info['视频拍摄'] = ''
        info['拍照特性'] = ''
    # video
    try:
        video = findcanshu(canshulist, 'typeName8')
        for li in video('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['视频格式'] = ''
        info['音乐格式'] = ''
        info['音乐特性'] = ''
        info['图片格式'] = ''
        info['文档格式'] = ''
    # location
    try:
        location = findcanshu(canshulist, 'typeName15')
        for li in location('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['GPS'] = ''
        info['感应器'] = ''
    # function
    try:
        func = findcanshu(canshulist, 'typeName16')
        for li in func('li'):
            tagnm = demess(li(class_='leftbiaoti')[0].text.encode('u8'))
            value = demess(li(class_='licont')[0].text.encode('u8'))
            info[tagnm] = value
    except:
        info['USB接口'] = ''
        info['耳机接口'] = ''
        info['无线连接'] = ''
        info['日常功能'] = ''
        info['键盘类型'] = ''
        info['输入方式'] = ''
        info['输入法'] = ''
        info['特殊功能'] = ''
    # nickname
    try:
        nickname = soup(class_='i_biao_down')[0]
        value = ''
        for li in nickname('li')[1:]:
            value += demess(li.text.encode('u8')) + ','
        info['网友还叫它'] = value
    except:
        info['网友还叫它'] = ''
    # write all info to output file
    write_info(model)
    # reset info to empty
    reset_info()


def reset_info():
    info = {}


def demess(s):
    return s.strip().replace('：', '').replace('\n', '').replace('|', '#')


def findcanshu(canshulist, idname):
    for c in canshulist:
        if c(id=idname):
            return c
    return None


def write_info(model):
    f = open(outfile, 'a')
    print >> f, model + '|' + '|'.join([info.get(key, '') for key in keys])
    f.close()
    

def run():
    with open(outfile, 'w') as f:
        print >> f, 'model|' + '|'.join(keys)
    files = glob.glob(outpath)
    for fn in files:
        get_info(fn)


def main():
    run()    


if __name__ == '__main__':
    main()

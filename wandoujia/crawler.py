#!/usr/bin/env python
#coding:utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import types
import urllib2
import json
#import MySQLdb
import time
import os

applist = './applist.csv'
if os.path.exists(applist):
	os.remove(applist)
log = './applist.log'

class tianqi:
	def __init__(self,page=1):
		self.page=page
		self.duan ="--------------------------"	#在控制台断行区别的

	#利用urllib2获取网络数据
	def registerUrl(self,tag):
		try:
			# url ="http://apps.wandoujia.com/api/v1/feeds?&max=10&start="+str((self.page-0)*10)+"&opt_fields=data.app.apks.versionName,data.app.apks.versionCode,data.app.title,data.app.packageName,data.app.appType,data.app.ad"
			url = "http://apps.wandoujia.com/api/v1/apps?ads_count=0&tag="+tag+"&max=10&start="+str((self.page-0)*10)+"&opt_fields=apps.apks.versionName,apps.apks.versionCode,apps.title,apps.packageName,apps.appType,apps.ad"
			#print url
			data = urllib2.urlopen(url,timeout=120).read()
			if(not data):
				#print "try again"
				data = urllib2.urlopen(url,timeout=180).read()
			return 200,data
		except Exception,e:
			if hasattr(e, 'code'):
				return e.code,[]
		# finally:
			# if data:
				# data.close()

	#写入文件
	def writeFile(self,fileData):
		file = open("json.txt","w")
		file.write(fileData)
		file.close()

	#解析从网络上获取的JSON数据	
	def parseJsonFile(self,jsonData):
		value = json.loads(jsonData)
		return value

	#插入数据库
	def insertMysql(self,json_data):
		try:
			conn=MySQLdb.connect(host='localhost',user='root',passwd='forthxu',port=3306)
			cur=conn.cursor()
			
			cur.execute('set names utf8')
			cur.execute('create database if not exists python DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci')
			conn.select_db('python')
			create_table_sql = """CREATE TABLE if not exists `app_versions` (
	`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
	`archive` int(10) NOT NULL DEFAULT '0' COMMENT '档案ID',
	`type` varchar(16) NOT NULL DEFAULT '' COMMENT '应用类型 software game 类型',
	`package` varchar(125) NOT NULL DEFAULT '' COMMENT '包名称 唯一',
	`version_code` int(10) NOT NULL DEFAULT '0',
	`version` varchar(16) NOT NULL DEFAULT '',
	`name` varchar(255) NOT NULL DEFAULT '' COMMENT '应用 名称',
	`addtime` int(10) NOT NULL DEFAULT '0',
	PRIMARY KEY (`id`),
	UNIQUE KEY `package_unqiue` (`package`) USING BTREE
	) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COMMENT='应用报名统计表'"""
			cur.execute(create_table_sql)
			
			# value=['game','package',10,'version','name']
			# cur.execute('insert into app_versions (`type`,`package`,`version_code`,`version`,`name`) values(%s,%s,%s,%s,%s)',value)
			
			values=[]
			for app in json_data[0]['apps']:
				value = (app['appType'].encode('utf-8'),app['packageName'].encode('utf-8'),app['apks'][0]['versionCode'],app['apks'][0]['versionName'].encode('utf-8'),app['title'].encode('utf-8'))
				values.append(value)
				print app['title'].encode('utf-8')#,app['packageName'].encode('utf-8')
				# if app['ad']==False:
					# cur.execute('insert ignore into app_versions (`type`,`package`,`version_code`,`version`,`name`) values(%s,%s,%s,%s,%s)',value)
					# conn.commit()
			
			cur.executemany('insert ignore into app_versions (`type`,`package`,`version_code`,`version`,`name`) values(%s,%s,%s,%s,%s)',values)
			conn.commit()
			
			
			cur.close()
			conn.close()
			
		except MySQLdb.Error,e:
			 print "Mysql Error %d: %s" % (e.args[0], e.args[1])
			 
	def query(self,tag,page):
		self.page =  page
		f = open(applist, 'a')
		l = open(log, 'a')
		while True:
			print >>l, '\n',tag,self.page,self.duan
			code,data = self.registerUrl(tag)
			if code != 200 :
				print >>l, 'error!',code
				break;
			json_data = self.parseJsonFile(data)
			# print json data
			if json_data[0]['apps'] and json_data[0]['apps'][0]:
				self.page+=1
				info=[]
				for app in json_data[0]['apps']:
					info.append(app['packageName'].encode('utf-8')+','+app['title'].encode('utf-8'))
				print >>f, '\n'.join(info)
				#self.insertMysql(json_data)
				time.sleep(0.2)
			else:
				break
		print >>l, "ok end"

if __name__ == "__main__":
	# print("-"*40)
	# print('输入开始页：')
	# print("-"*40)
	# xinput = raw_input()
	
	# "休闲时间","跑酷竞速","宝石消除","网络游戏","动作射击","扑克棋牌","儿童益智","塔防守卫","体育格斗","角色扮演","经营策略","影音图像","通信聊天","网上购物","美化手机","阅读学习","便捷生活","常用工具","出行必用","性能优化","新闻资讯","社交网络","金融理财","办公软件","育儿母婴"
	
	# 
	tianqi=tianqi(1)
	#tags1=["影音图像","通信聊天","网上购物","美化手机","阅读学习","便捷生活","常用工具","出行必用","性能优化","新闻资讯","社交网络","金融理财","办公软件","育儿母婴"]
	tags1=["视频","音乐","图像","新闻阅读","生活实用工具","系统工具","美化手机","效率办公","聊天社交","电话通讯","交通导航","旅游出行","购物","生活服务","运动健康","教育培训","金融理财","丽人母婴","影音图像","通信聊天","网上购物","阅读学习","便捷生活","常用工具","出行必用","性能优化","新闻资讯","社交网络","出行必用","性能优化","新闻资讯","社交网络","金融理财","办公软件","育儿母婴"]
	tags2=["休闲时间","跑酷竞速","宝石消除","网络游戏","动作射击","扑克棋牌","儿童益智","塔防守卫","体育格斗","角色扮演","经营策略"]
	tags3=[]
	tags=tags1+tags2
	for tag in tags:
		tianqi.query(tag,1)
		time.sleep(3)
	
	

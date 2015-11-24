from selenium import webdriver
from datetime import datetime
import time

time.sleep(15)

d = webdriver.Firefox()
d.get('http://www.baidu.com')
#d.get('http://sj.qq.com/myapp/category.htm?orgame=2')
print >> open('/home/ziye/Documents/crawler/multi_store_game/test', 'w'), datetime.now().strftime('%Y-%m-%d %H-%M-%S'), d.title.encode('u8')
d.quit()

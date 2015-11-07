from pyvirtualdisplay import Display
from selenium import webdriver

print 'start'

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://www.baidu.com')
print browser.title
browser.quit()

display.stop()

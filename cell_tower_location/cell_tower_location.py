__author__ = 'ziye'


from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://www.gpsspg.com/bs.htm')

driver.find_element_by_id('u_mcc').send_keys('460')
driver.find_element_by_id('u_mnc').send_keys('01')
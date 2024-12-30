# author：辣条
# ide： PyCharm

from selenium import webdriver
import datetime	
import time

#自动打开浏览器并且最大化窗口
driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://www.taobao.com')

if driver.find_element_by_partial_link_text('亲，请登录'):
        driver.find_element_by_partial_link_text('亲，请登录').click()
#跳转到购物车页面
driver.get('https://cart.taobao.com/cart.htm')

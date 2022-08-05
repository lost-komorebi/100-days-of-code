#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver = '/Users/whatthefuck/Applications/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


timeout1 = time.time() + 5  # 5 seconds from now
timeout2 = time.time() + 60 * 5  # 5 minutes from now
while True:
    driver.find_element(By.ID, 'cookie').click()
    if time.time() > timeout1:
        items = driver.find_elements(By.CSS_SELECTOR, '#store div')
        max_index = 0
        for item in items:  # 获取最贵的商品并购买
            if not item.get_attribute('class'):
                if items.index(item) > max_index:
                    max_index = items.index(item)
        items[max_index].click()
        timeout1 = timeout1 + 5  # 超时加上5秒，使继续点击cookies
    if time.time() > timeout2:
        print(driver.find_element(By.ID, 'money').text)
        break

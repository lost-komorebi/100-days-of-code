#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = '/Users/whatthefuck/Applications/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.python.org/")

events = driver.find_elements(
    By.CSS_SELECTOR,
    '.event-widget .shrubbery .menu li a')
times = driver.find_elements(By.CSS_SELECTOR,
                             '.event-widget .shrubbery .menu li time')
results = {}
print([{time.text: event.text} for time, event in zip(times, events)])

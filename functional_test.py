'''
Created on 2017年3月30日

@author: xixi
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('localhost:8000')

assert 'Django' in browser.title
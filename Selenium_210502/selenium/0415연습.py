
# from urllib.request import urlopen
# # from bs4 import BeautifulSoup
# # import re

# # html = urlopen('https://www.naver.com/')
# # bs = BeautifulSoup(html, 'html.parser')
# # for link in bs.findAll('o'):
# #     if 'i' in link.attrs:
# #         print(link.attrs['i'])

# import requests
# from bs4 import BeautifulSoup
# req = requests.get("https://map.naver.com/v5/directions/14132510.138067331,4505514.899798114,%EB%B6%80%EB%AF%B8%EC%95%84%EB%9D%A0%EB%9E%91%EC%8A%A4%ED%9E%90,18695277,PLACE_POI/14127234.017217796,4511170.18261268,%EC%98%81%EB%93%B1%ED%8F%AC%EC%97%AD%20%EA%B2%BD%EB%B6%80%EC%84%A0(%EA%B3%A0%EC%86%8D%EC%B2%A0%EB%8F%84),19546238,PLACE_POI/-/transit?c=14125155.7462899,4508519.1717988,12,0,0,0,dh")
# req.text
# soup = BeautifulSoup(req.content, "html.parser")
# soup.find_all("div")
#  elem = driver.find_element_by_class_name(
#         "item_summary ng-star-inserted")
#     print(elem)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request
import os

# 포인트 읽기
f = open("포인트.txt", 'r', encoding='utf8')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://map.naver.com/v5/directions/14127234.017217796,4511170.18261268,%EC%98%81%EB%93%B1%ED%8F%AC%EC%97%AD%20%EA%B2%BD%EB%B6%80%EC%84%A0(%EA%B3%A0%EC%86%8D%EC%B2%A0%EB%8F%84),19546238,PLACE_POI/14133569.61018901,4507759.09256961,%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EB%8F%99%EC%9E%91%EA%B5%AC%20%EC%82%AC%EB%8B%B9%EB%8F%99%20183-15,,/-/transit?c=14128477.3125844,4509647.0656605,13,0,0,0,dh")
time.sleep(0.2)
# title = bs.findAll(id='title',class_='text')
fnltime = driver.find_element_by_css_selector(
    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(1) > strong > readable-duration")
walktime = driver.find_element_by_css_selector(
    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(2) > readable-duration")
fnlcost = driver.find_element_by_css_selector(
    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(3)")
print(fnltime.text)
print(walktime.text)
print(fnlcost.text)

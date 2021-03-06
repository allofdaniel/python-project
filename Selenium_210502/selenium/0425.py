# python selenium example

# python selenium example

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request
import os
# import openpyxl
from tqdm import tqdm


tic = time.time()

options = webdriver.ChromeOptions()
options.add_argument('headless')  # headless
options.add_argument('window-size=1920x1080')  # headless
options.add_argument("disable-gpu")  # headless
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    executable_path='C:/Users/allof/OneDrive/바탕 화면/matlab_Python Study/Python-git/Selenium_210502/chromedriver.exe', options=options)
driver.implicitly_wait(3)  # imp wt

# 포인트 읽기
f = open('포인트.txt', 'r', encoding='utf8')
lines = f.readlines(int())

# 대중교통
for idx_org_, org_ in tqdm(enumerate(lines)):
    for idx_des_, des_ in enumerate(lines):
        if idx_org_ != idx_des_:
            driver.get(
                "https://map.naver.com/v5/directions/{0},%EC%B6%9C%EB%B0%9C%EC%A7%80,,/{1},%EB%8F%84%EC%B0%A9%EC%A7%80,,ADDRESS_POI/-/transit?c=14110045.8089916,4510631.0916025,10,0,0,0,dh".format(org_, des_))
            try:
                # time.sleep(1)
                time_p = driver.find_element_by_css_selector(
                    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(1) > strong > readable-duration")
                walktime_p = driver.find_element_by_css_selector(
                    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(2) > readable-duration")
                cost_p = driver.find_element_by_css_selector(
                    "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(3)")
            except:
                text = open('테스트.txt', 'a')
                text.write("zone{} to zone{} 결과없음\n".format(
                    idx_org_, idx_des_))
                pass
            else:
                a_p = time_p.text
                b_p = walktime_p.text
                c_p = cost_p.text
                text = open('테스트.txt', 'a')
                text.write("zone{} to zone{}".format(idx_org_, idx_des_))
                text.write(' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
            # finally:
            #     text.close()
            #     driver.quit()
        else:
            text = open('테스트.txt', 'a')
            text.write("zone{} to zone{} 동일경로\n".format(idx_org_, idx_des_))
            text.close()

toc = time.time()
print(toc-tic)

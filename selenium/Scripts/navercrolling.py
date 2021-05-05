# python selenium example

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request

# 존체계 읽기
f = open("존체계.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://map.naver.com/v5/")
    # ID 입력
    time.sleep(1)
    elem = driver.find_element_by_xpath(
        "/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-input-box/div/div[1]/div/input")
    time.sleep(1)
    elem.send_keys(line)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    a = driver.current_url

    ad_st_pt = a.find("address")
    ad_st_pt_2 = a.find(",", ad_st_pt)  # 145
    ad_st_pt_3 = a.find(",", ad_st_pt_2+1)  # 164

    st_pt = ad_st_pt+8
    end_pt = ad_st_pt_3-1
    point_ = a[st_pt:end_pt]
    text = open('지금.txt', 'a')
    text.write(str(point_))
    text.write('\n')
    text.close()
    driver.quit()

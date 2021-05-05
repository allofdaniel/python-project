# python selenium example

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request

# 포인트 읽기
f = open("포인트.txt", 'r', encoding='utf8')
lines = f.readlines()
for line in lines:

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://map.naver.com/v5/")
    # https://map.naver.com/v5/directions/14122283.105128657,4535450.127926778,%EC%B6%9C%EB%B0%9C%EC%A7%80,,/14115800.659485195,4485809.476330541,%EB%8F%84%EC%B0%A9%EC%A7%80,,ADDRESS_POI/-/transit?c=14110045.8089916,4510631.0916025,10,0,0,0,dh 길찾기 대중교통
    # https://map.naver.com/v5/directions/14122283.105128657,4535450.127926778,%EC%B6%9C%EB%B0%9C%EC%A7%80,,/14115800.659485195,4485809.476330543,%EB%8F%84%EC%B0%A9%EC%A7%80,,ADDRESS_POI/-/car?c=14102134.8779311,4511428.0649335,10,0,0,0,dh 길찾기 자동차
    # https://map.naver.com/v5/directions/14122283.105128657,4535450.127926778,%EC%B6%9C%EB%B0%9C%EC%A7%80,,/14115800.659485195,4485809.476330543,%EB%8F%84%EC%B0%A9%EC%A7%80,,ADDRESS_POI/-/walk?c=14102134.8779311,4511428.0649335,10,0,0,0,dh 길찾기 도보
    # https://map.naver.com/v5/directions/14122283.105128657,4535450.127926778,%EC%B6%9C%EB%B0%9C%EC%A7%80,,/14115800.659485195,4485809.476330543,%EB%8F%84%EC%B0%A9%EC%A7%80,,ADDRESS_POI/-/bike?c=14102134.8779311,4511428.0649335,10,0,0,0,dh 길찾기 자전거
    # selenium tab을 이용하여 구글탭으로 검색. + beautifulsoup4로 데이터 추출(가능한 전부)코드 밑에.
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

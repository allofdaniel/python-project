import os
from datetime import datetime, timezone, timedelta

import boto3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


BUCKET_NAME = os.getenv('mywebcrolling', '')


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # headless
    options.add_argument('window-size=1920x1080')  # headless
    options.add_argument("disable-gpu")  # headless
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        executable_path='C:/Users/allof/OneDrive/바탕 화면/matlab_Python Study/Python-git/Selenium_210502/chromedriver.exe', options=options)
    driver.implicitly_wait(3)
    return driver

# 대중교통


def crolling_cost_in_naver(driver, lines, result_list):
    for idx_org_, org_ in enumerate(lines):
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
                    result_list.append(
                        "zone{} to zone{} 결과없음\n".format(idx_org_, idx_des_))
                    pass
                else:
                    a_p = time_p.text
                    b_p = walktime_p.text
                    c_p = cost_p.text
                    result_list.append(
                        "zone{} to zone{}".format(idx_org_, idx_des_))
                    result_list.append(
                        ' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
            else:
                result_list.append(
                    "zone{} to zone{} 동일경로\n".format(idx_org_, idx_des_))
    return result_list


def lambda_handler(event, context):
    tz = timezone(timedelta(hours=9))
    kst_dt = datetime.now().astimezone(tz)
    date_str = kst_dt.strftime('%Y%m%d')

    driver = get_driver()
    result_list = []
    lines = ['14135553.323514942,4520966.74856530',
             '14135882.339401934,4520271.26475237', '14134308.315197963,4520843.69298269']
    contents = crolling_cost_in_naver(driver, lines, result_list)
    # write_to_s3(date_str, 'navercrolling', ''.join(contents))
    #print(date_str, 'navercrolling', ''.join(contents))

    driver.close()
    return contents

# lambda_handler(1,1)

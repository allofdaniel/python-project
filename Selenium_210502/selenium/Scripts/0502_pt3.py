import json
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')a
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = "/opt/python/bin/headless-chromium"
    driver = webdriver.Chrome(
        '/opt/python/bin/chromedriver', chrome_options=chrome_options)
    driver.implicitly_wait(3)
    return driver


lines = ['14135553.323514942,4520966.74856530',
         '14135882.339401934,4520271.26475237', '14134308.315197963,4520843.69298269']
result_list = []


def write_to_s3(date_str, news_type, data: str):
    encoded_string = data.encode('utf-8')
    file_name = f'{date_str}.txt'
    s3_path = f'{news_type}/' + file_name
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).put_object(Key=s3_path, Body=encoded_string)


def lambda_handler(event, context):
    # 대중교통
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
    return {
        'statusCode': 200,
        'body': json.dumps(result_list)
    }

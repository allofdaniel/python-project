# lambd 베끼기

import os
from datetime import datetime, timezone, timedelta
import json

import boto3
import botocore
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_driver():
    options = webdriver.ChromeOptions()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
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

# 대중교통 ( 0-326, 327-653, 654-980, 981-)


def crolling_cost_in_naver(driver, filename, lines, result_list):
    for idx_org_, org_ in enumerate(lines):
        if idx_org_ == filename:
            for idx_des_, des_ in enumerate(lines):
                if idx_org_ != idx_des_ and 0 = < idx_des_ = < 3:
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
        else:
            pass
    return result_list


def lambda_handler(event, context):


s3 = boto3.client("s3")
   if event:
        file_obj = event["Records"][0]
        filename = str(file_obj["s3"]["object"]["key"])
        bucket = file_obj['s3']['bucket']['name']
        print("File name : ", filename)

        file_obj = s3.get_object(Bucket=bucket, Key=filename)

        file_content = file_obj["Body"].read().decode("utf-8")
        print("File content : ", file_content)

        lines = file_content.readlines(int())

        driver = get_driver()
        result_list = []
        contents = crolling_cost_in_naver(driver, filename, lines, result_list)
        driver.close()

        lambda_path = "/tmp/1.txt"

        with open(lambda_path, 'w+') as file:
            file.write(contents)
            file.close()

        # automatically generate sub direcotry....
        s3.upload_file(lambda_path, bucket, "sub/"+filename+".txt")

    return {'statusCode': 200, 'body': json.dumps(contents) }

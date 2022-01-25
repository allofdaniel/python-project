import os
from datetime import datetime, timezone, timedelta
import json
import time
import boto3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


# BUCKET_NAME = os.getenv('mywebcrolling', '')


# 	Billed Duration: 14158 ms	Memory Size: 10240 MB
# 	Billed Duration: 17462 ms	Memory Size: 2048 MB
# 	Billed Duration: 33672 ms	Memory Size: 1024 MB	Max Memory Used: 553 MB	Init Duration: 292.54 ms

# def get_txt_from_bucket():
# def save_txt_to_bucket():

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
    # chrome_options.add_argument(
    #     'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    # chrome_options.binary_location = "/opt/python/bin/headless-chromium"
    # driver = webdriver.Chrome(
    #     '/opt/python/bin/chromedriver', chrome_options=chrome_options)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        executable_path='C:/Users/allof/OneDrive/바탕 화면/matlab_Python Study/Python-git/Selenium_210502/chromedriver.exe', options=options)
    driver.implicitly_wait(3)
    return driver

# 대중교통


def crolling_cost_in_naver(driver, lines, result_list):
    for idx_org_, org_ in enumerate(lines):
        if idx_org_ == 0:
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
                        text = open('대중교통.txt', 'a')
                        text.write("zone{} to zone{} 결과없음\n".format(
                            idx_org_, idx_des_))
                        result_list.append(
                            "zone{} to zone{} 결과없음\n".format(idx_org_, idx_des_))
                        pass
                    else:
                        a_p = time_p.text
                        b_p = walktime_p.text
                        c_p = cost_p.text
                        text = open('대중교통.txt', 'a')
                        text.write("zone{} to zone{}".format(
                            idx_org_, idx_des_))
                        text.write(
                            ' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
                        result_list.append(
                            "zone{} to zone{}".format(idx_org_, idx_des_))
                        result_list.append(
                            ' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
                else:
                    text = open('대중교통.txt', 'a')
                    text.write("zone{} to zone{} 동일경로\n".format(
                        idx_org_, idx_des_))
                    text.close()
                    result_list.append(
                        "zone{} to zone{} 동일경로\n".format(idx_org_, idx_des_))
        else:
            pass
    for idx_org_, org_ in enumerate(lines):
        if idx_org_ == 0:
            for idx_des_, des_ in enumerate(lines):
                if idx_org_ != idx_des_:
                    driver.get(
                        "https://map.naver.com/v5/directions/{0},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EC%B2%AD%EC%9A%B4%ED%9A%A8%EC%9E%90%EB%8F%99,,/{1},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EA%B0%80%ED%9A%8C%EB%8F%99,,/-/car?c=14135277.4956642,4520807.1271698,15,0,0,0,dh".format(org_, des_))
                    try:
                        fnltime_car = driver.find_element_by_css_selector(
                            "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > strong > readable-duration")
                        distance_car = driver.find_element_by_css_selector(
                            "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > span.summary_text > readable-distance")
                        tollfee = driver.find_element_by_css_selector(
                            "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(1)")
                        gasprice = driver.find_element_by_css_selector(
                            "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(2) > span")
                        taxicost = driver.find_element_by_css_selector(
                            "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(3) > span")
                    except:
                        text = open('자동차.txt', 'a')
                        text.write("zone{} to zone{} 결과없음\n".format(
                            idx_org_, idx_des_))
                        pass
                    else:
                        a_c = fnltime_car.text
                        b_c = distance_car.text
                        c_c = tollfee.text
                        d_c = gasprice.text
                        e_c = taxicost.text
                        text = open('자동차.txt', 'a')
                        text.write("zone{} to zone{}".format(
                            idx_org_, idx_des_))
                        text.write(' 총 {}, 거리 {}, {}, 주유비 {}, 택시비 {}\n'.format(
                            a_c, b_c, c_c, d_c, e_c))
                    # finally:
                    #     text.close()
                    #     driver.quit()
                else:
                    text = open('자동차.txt', 'a')
                    text.write("zone{} to zone{} 동일경로\n".format(
                        idx_org_, idx_des_))
                    text.close()
    return result_list


def lambda_handler(event, context):
    tic = time.time()

    tz = timezone(timedelta(hours=9))
    kst_dt = datetime.now().astimezone(tz)
    date_str = kst_dt.strftime('%Y%m%d')

    driver = get_driver()
    result_list = []
    f = open('포인트.txt', 'r', encoding='utf8')
    lines = f.readlines(int())
    # lines = ['14135553.323514942,4520966.74856530',
    #             '14135882.339401934,4520271.26475237', '14134308.315197963,4520843.69298269']
    contents = crolling_cost_in_naver(driver, lines, result_list)
    # write_to_s3(date_str, 'navercrolling', ''.join(contents))

    driver.close()
        tic = time.time()
    toc = time.time()
    print(toc-tic)
    # return { 'statusCode': 200, 'body': json.dumps(contents) }
    return contents


lambda_handler(1, 1)

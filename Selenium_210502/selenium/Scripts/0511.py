import botocore
import os
from datetime import datetime, timezone, timedelta
import json

import boto3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


BUCKET_NAME = os.getenv('mywebcrolling', '')


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


def write_to_s3(date_str, news_type, data: str):
    encoded_string = contents.encode('utf-8')
    file_name = f'{date_str}.txt'
    s3_path = f'{news_type}/' + file_name

    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).put_object(Key=s3_path, Body=encoded_string)


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

    driver.close()
    write_to_s3(date_str, 'popular_day', ''.join(contents))
    return contents

    # lambda 로 s3 bucket list 출력
    import json


def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket_list = []
    for bucket in s3.buckets.all():
        bucket_list.append(bucket.name)

    return json.dumps(bucket_list)

    # lambda의 txt 읽어오기


def lambda_handler(event, context):
    bucket_name = 'mywebcrolling'
    key = 'point.txt'

    s3_client = boto3.client('s3')

    data = s3_client.get_object(Bucket=bucket_name, Key=key)
    file_txt = data['Body'].read()

    return json.dumps(file_txt.decode('UTF-8'))

#     #lambda img 읽어와서 resize 후 저장 (PIL LAYER 필요)
# import boto3
# import os
# import sys
# import uuid
# from urllib.parse import unquote_plus
# from PIL import Image
# import PIL.Image

# s3_client = boto3.client(' s3 ' )

# def resize_image(image_path, resized_path):
#     with Image.open(imag_path) as image:
#         image.thumbnail(tuple(x / 2 for x in image.size))
#         image.save(resized_path)

# def lambda_handler(event, context):
#     for record in event['Records']:
#     bucket = record [ ' s3 ' ] [ ' bucket ' ] [ ' name ' ]
#     key = unquote_plus(record['s3']['object'] [ ' key ' ] )
#     tmpkey = key. replace( ' / ' , ' ' )
#     download_path = '/tmp/{}{}' .format(uuid.uuid4(), tmpkey)
#     upload_path = ' /tmp/resized-{}'.format(tmpkey)
#     s3_client.download_file(bucket, key, download_path)
#     resize_image(download_path, upload_path)
#         s3_client.upload_file (upload_path,'{ }-resiz.ed '.format(bucket), key)

# s3 /sub에 txt 읽고 저장


s3 = boto3.client("s3")


def lambda_handler(event, context):

    print("I'm triggered !!")

    if event:
        file_obj = event["Records"][0]
        filename = str(file_obj["s3"]["object"]["key"])
        bucket = file_obj['s3']['bucket']['name']
        print("File name : ", filename)

        file_obj = s3.get_object(Bucket=bucket, Key=filename)

        file_content = file_obj["Body"].read().decode("utf-8")
        print("File content : ", file_content)

        lambda_path = "/tmp/1.txt"

        with open(lambda_path, 'w+') as file:
            file.write(file_content+" ...YOLO!")
            file.close()

        # automatically generate sub direcotry....
        s3.upload_file(lambda_path, bucket, "sub/result.txt")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    # 내가만든 code  s3 불러와서 s3 저장

    import json


def read_txt_from_s3():
    bucket_name = 'mywebcrolling'
    key = 'test.txt'
    s3_client = boto3.client('s3')
    data = s3_client.get_object(Bucket=bucket_name, Key=key)
    file_txt = data['Body'].read().decode("utf-8")
    return file_txt


def write_txt_to_s3(file_txt):
    bucket_name = 'mywebcrolling'
    s3 = boto3.client("s3")
    lambda_path = "/tmp/1.txt"

    with open(lambda_path, 'w+') as file:
        file.write(file_txt+" ...YOLO!")
        file.close()
    s3.upload_file(lambda_path, bucket_name, "sub/result3.txt")


def lambda_handler(event, context):
    file_txt = read_txt_from_s3()

    write_txt_to_s3(file_txt)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

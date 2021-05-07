import os
from datetime import datetime, timezone, timedelta
import boto3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


BUCKET_NAME = os.getenv('mywebcrolling', '')


# def get_driver():
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
driver = webdriver.Chrome('/opt/python/bin/chromedriver',
                          chrome_options=chrome_options)
return driver

# _SECTIONS = {
#     '100': '정치',
#     '101': '경제',
#     '102': '사회',
#     '103': '생활/문화',
#     '104': '세계',
#     '105': 'IT/과학'
# }

# def write_to_s3(date_str, news_type, data: str):
#     encoded_string = data.encode('utf-8')
#     file_name = f'{date_str}.txt'
#     s3_path = f'{news_type}/' + file_name

#     s3 = boto3.resource('s3')
#     s3.Bucket(BUCKET_NAME).put_object(Key=AKIAYBJONTBBCMERFASA, Body=encoded_string)


# def get_popular_day_news_contents(driver, date_str, section_id):
#     url = f'https://news.naver.com/main/ranking/popularDay.nhn' \
#         f'?rankingType=popular_day' \
#         f'&sectionId={section_id}&date={date_str}'
#     driver.get(url)
#     driver.implicitly_wait(1)

#     ranking = driver.find_elements_by_class_name('ranking')

#     if ranking:
#         headlines = ranking[0].find_elements_by_class_name('ranking_headline')
#         ledes = ranking[0].find_elements_by_class_name('ranking_lede')
#         offices = ranking[0].find_elements_by_class_name('ranking_office')
#         views = ranking[0].find_elements_by_class_name('ranking_view')
#         return zip(headlines, ledes, offices, views)
#     else:
#         return None


# tz = timezone(timedelta(hours=9))
# kst_dt = datetime.now().astimezone(tz)
# date_str = kst_dt.strftime('%Y%m%d')

# driver = get_driver()

# columns = ['date', 'section', 'office', 'view', 'headline', 'lede', 'link']
# data = []
# data.append('\t'.join(columns) + '\n')

# for section_id, section_name in _SECTIONS.items():
#     contents = get_popular_day_news_contents(driver, date_str, section_id)
#         if contents:
#             for headline, lede, office, view in contents:
#                 headline_a_tag = headline.find_element_by_tag_name('a')
#                 contents = '\t'.join([
#                     date_str,
#                     section_name,
#                     office.text,
#                     view.text,
#                     headline_a_tag.get_attribute('title'),
#                     lede.text,
#                     headline_a_tag.get_attribute('href')
#                 ])
#                 data.append(contents + '\n')
# write_to_s3(date_str, 'popular_day', ''.join(data))

# driver.close()

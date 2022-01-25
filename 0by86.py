
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


tic = time.time()

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
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    executable_path='C:/chromedriver.exe', options=options)
driver.implicitly_wait(3)


f = open("포인트.txt", 'r', encoding='utf8')
lines = f.readlines(int())


# 대중교통 link_tab bike
for idx_org_, org_ in enumerate(lines):
    # if 0 <= idx_org_ <= 27:
    for idx_des_, des_ in enumerate(lines):
        if idx_org_ != idx_des_:
            driver.get(
                "https://map.naver.com/v5/directions/{0},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%84%9C%EB%8C%80%EB%AC%B8%EA%B5%AC%20%EC%8B%A0%EC%B4%8C%EB%8F%99,,/{1},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EA%B0%80%ED%9A%8C%EB%8F%99,,/-/transit?c=14110410.1912547,4521849.3636262,10,0,0,0,dh".format(org_, des_))
            driver.find_element_by_css_selector(
                "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > directions-summary-list-timeset > div > div.timeset_option.timeset_option_hour > div > div > div > ul > li:nth-child(9) > button").click()
            driver.find_element_by_css_selector(
                "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > directions-summary-list-timeset > div > div.timeset_option.timeset_option_minute > div > div > div > ul > li:nth-child(1) > button").click()
            driver.find_element_by_css_selector(
                "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > div.departure_info > span > button > span").click()
            driver.implicitly_wait(3)
            try:
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
                pass
            else:
                a_p = time_p.text
                b_p = walktime_p.text
                c_p = cost_p.text
                text = open('대중교통.txt', 'a')
                text.write("zone{} to zone{}".format(idx_org_, idx_des_))
                text.write(' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
        else:
            text = open('대중교통.txt', 'a', encoding='utf8')
            text.write("zone{} to zone{} 동일경로\n".format(
                idx_org_, idx_des_))
            text.close()
# else:
#     pass

# 8시
# container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > directions-summary-list-timeset > div > div.timeset_option.timeset_option_hour > div > div > div > ul > li:nth-child(9) > button
# 00분
# container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > directions-summary-list-timeset > div > div.timeset_option.timeset_option_minute > div > div > div > ul > li:nth-child(1) > button

# "https://map.naver.com/v5/directions/{0},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%84%9C%EB%8C%80%EB%AC%B8%EA%B5%AC%20%EC%8B%A0%EC%B4%8C%EB%8F%99,,/{1},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EA%B0%80%ED%9A%8C%EB%8F%99,,/-/transit?c=14110410.1912547,4521849.3636262,10,0,0,0,dh".format(org_, des_))

# # 자동차 link_tab bike
# for idx_org_, org_ in enumerate(lines):
#     if 26 <= idx_org_ <= 27:
#         for idx_des_, des_ in enumerate(lines):
#             if idx_org_ != idx_des_:
#                 driver.get(
#                     "https://map.naver.com/v5/directions/{0},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EC%B2%AD%EC%9A%B4%ED%9A%A8%EC%9E%90%EB%8F%99,,/{1},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EA%B0%80%ED%9A%8C%EB%8F%99,,/-/bike?c=14134599.1170381,4520558.7068279,15,0,0,0,dh".format(org_, des_))
#                 try:
#                 fnltime_car = driver.find_element_by_css_selector(
#                     "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > strong > readable-duration")
#                 distance_car = driver.find_element_by_css_selector(
#                     "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > span.summary_text > readable-distance")
#                 tollfee = driver.find_element_by_css_selector(
#                     "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(1)")
#                 gasprice = driver.find_element_by_css_selector(
#                     "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(2) > span")
#                 taxicost = driver.find_element_by_css_selector(
#                     "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(3) > span")
#             except:
#                 text = open('자동차.txt', 'a')
#                 text.write("zone{} to zone{} 결과없음\n".format(
#                     idx_org_, idx_des_))
#                 pass
#             else:
#                 a_c = fnltime_car.text
#                 b_c = distance_car.text
#                 c_c = tollfee.text
#                 d_c = gasprice.text
#                 e_c = taxicost.text
#                 text = open('자동차.txt', 'a')
#                 text.write("zone{} to zone{}".format(idx_org_, idx_des_))
#                 text.write(' 총 {}, 거리 {}, {}, 주유비 {}, 택시비 {}\n'.format(
#                     a_c, b_c, c_c, d_c, e_c))
#         else:
#             text = open('자동차.txt', 'a')
#             text.write("zone{} to zone{} 동일경로\n".format(idx_org_, idx_des_))
#             text.close()
#     else:
#         pass


toc = time.time()
print(toc-tic)


# # 대중교통 + 자동차
# for idx_org_, org_ in enumerate(lines):
#     if 26 <= idx_org_ <= 86:
#         for idx_des_, des_ in enumerate(lines):
#             if idx_org_ != idx_des_:
#                 driver.get(
#                     "https://map.naver.com/v5/directions/{0},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EC%B2%AD%EC%9A%B4%ED%9A%A8%EC%9E%90%EB%8F%99,,/{1},%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%A2%85%EB%A1%9C%EA%B5%AC%20%EA%B0%80%ED%9A%8C%EB%8F%99,,/-/bike?c=14134599.1170381,4520558.7068279,15,0,0,0,dh".format(org_, des_))
#                 driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-summary-list-transit-option > div > div.departure_info > span > button > span").click()
#                 try:
#                     time_p = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(1) > strong > readable-duration")
#                     walktime_p = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(2) > readable-duration")
#                     cost_p = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-pubtransit.item_summary.selected.ng-star-inserted > div:nth-child(2) > span:nth-child(3)")
#                 except:
#                     text = open('대중교통.txt', 'a')
#                     text.write("zone{} to zone{} 결과없음\n".format(
#                         idx_org_, idx_des_))
#                     pass
#                 else:
#                     a_p = time_p.text
#                     b_p = walktime_p.text
#                     c_p = cost_p.text
#                     text = open('대중교통.txt', 'a')
#                     text.write("zone{} to zone{}".format(idx_org_, idx_des_))
#                     text.write(' 총 {}, 도보 {}, 비용 {}\n'.format(a_p, b_p, c_p))
#                 #자동차
#                 try:
#                     driver.find_element_by_css_selector(
#                             "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > div > ul > li.item_tab.active > a").click()
#                     fnltime_car = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > strong > readable-duration")
#                     distance_car = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.summary_box > span.summary_text > readable-distance")
#                     tollfee = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(1)")
#                     gasprice = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(2) > span")
#                     taxicost = driver.find_element_by_css_selector(
#                         "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-car.item_summary.selected.ng-star-inserted > div.route_text_box.fee > span:nth-child(3) > span")
#                 except:
#                     text = open('자동차.txt', 'a')
#                     text.write("zone{} to zone{} 결과없음\n".format(
#                         idx_org_, idx_des_))
#                     pass
#                 else:
#                     a_c = fnltime_car.text
#                     b_c = distance_car.text
#                     c_c = tollfee.text
#                     d_c = gasprice.text
#                     e_c = taxicost.text
#                     text = open('자동차.txt', 'a')
#                     text.write("zone{} to zone{}".format(idx_org_, idx_des_))
#                     text.write(' 총 {}, 거리 {}, {}, 주유비 {}, 택시비 {}\n'.format(
#                         a_c, b_c, c_c, d_c, e_c))
#             else:
#                 text = open('대중교통0-86.txt', 'a', encoding='utf8')
#                 text.write("zone{} to zone{} 동일경로\n".format(
#                     idx_org_, idx_des_))
#                 text.close()
#                 text = open('자동차.txt', 'a')
#                 text.write("zone{} to zone{} 동일경로\n".format(idx_org_, idx_des_))
#                 text.close()
#     else:
#         pass

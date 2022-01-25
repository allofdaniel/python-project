import os
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

tic = time.time()

options = webdriver.ChromeOptions()
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
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
    # 'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
chrome_options.binary_location="/opt/python/bin/headless-chromium"
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver=webdriver.Chrome(
    executable_path='C:/chromedriver.exe', options=options)


f=open("포인트.txt", 'r', encoding='utf8')
lines=f.readlines(int())

for idx_org_, org_ in enumerate(lines):
    if 639 <= idx_org_ <= 695:
        for idx_des_, des_ in enumerate(lines):
            if idx_org_ != idx_des_:
                driver.implicitly_wait(2)
                driver.get(
                    "https://map.naver.com/v5/directions/{0},%EC%84%B1%EB%82%A8%EC%8B%9C%EC%B2%AD,11627831,PLACE_POI/{1},%EC%96%91%EC%82%B0%EC%8B%9C%EC%B2%AD,11628231,PLACE_POI/-/walk?c=14022253.5341211,4351060.4882194,6,0,0,0,dh".format(org_, des_))
                try:
                    fnltime_wlk=driver.find_element_by_css_selector(
                        "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-walking.item_summary.selected.ng-star-inserted > div.summary_box > strong > readable-duration")
                    distance_wlk=driver.find_element_by_css_selector(
                        "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-walking.item_summary.selected.ng-star-inserted > div.summary_box > span.summary_text > readable-distance")
                    path_wlk=driver.find_element_by_css_selector(
                        "#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-summary-list > directions-hover-scroll > div > div > directions-summary-item-walking.item_summary.selected.ng-star-inserted > div.route_box.ng-star-inserted > div > span > directions-facilities")
                except:
                    if driver.find_element_by_css_selector("#container > shrinkable-layout > div > directions-layout > directions-result > div.main > directions-error > div > p > span").text == "출발지와 도착지 간의 직선거리가 50km 이내인 경우만 도보 길찾기를 제공합니다.":
                        text=open('도보-695.txt', 'a', encoding='utf8')
                        text.write("zone{} to zone{} 측정불가\n".format(
                            idx_org_, idx_des_))
                        pass
                    else:
                        text=open('도보-695.txt', 'a', encoding='utf8')
                        text.write("zone{} to zone{} 시간초과\n".format(
                            idx_org_, idx_des_))
                else:
                    a_w=fnltime_wlk.text
                    b_w=distance_wlk.text
                    c_w=path_wlk.text
                    text=open('도보-695.txt', 'a', encoding='utf8')
                    text.write("zone{} to zone{}".format(
                        idx_org_, idx_des_))
                    text.write(
                        ' 총 {}, 거리 {}, 경로 {}\n'.format(a_w, b_w, c_w))
            else:
                text=open('도보-695.txt', 'a', encoding='utf8')
                text.write("zone{} to zone{} 동일경로\n".format(
                    idx_org_, idx_des_))
                text.close()
    else:
        pass
toc=time.time()
print(toc-tic)

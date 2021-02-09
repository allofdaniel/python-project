# python selenium example

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  # 시간차 위해 적용
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://hanseoatl.com/board/bbs/login.php?wr_id=&url=%2Fboard%2Fbbs%2Fboard.php%3Fbo_table%3Dlpds%26wr_id%3D")
# ID 입력
elem = driver.find_element_by_name("mb_id")
elem.send_keys("visbok")
# PW 입력
elem = driver.find_element_by_name("mb_password")
elem.send_keys("tjdrhd12")
elem.send_keys(Keys.RETURN)

# SCROLL_PAUSE_TIME = 1

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height


# # 'python selenium 엔터'/'python selenium enter' 이렇게 검색시 나옴.

# site = driver.find_elements_by_link_text("")
# site = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

i = 2
j = 2

while i in range(2, 12):
    elems = driver.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr["+str(i)+"]/td[2]/nobr/a")
    elems.click()
    while j in range(2, 6, 1):
        filedown = driver.find_element_by_xpath(
            "/html/body/div[3]/div[2]/div/table[1]/tbody/tr/td/table/tbody/tr["+str(j)+"]/td/a/span[1]")
        filedown.click()
        j += 1
        time.sleep(1)
    else:
        time.sleep(1)
        driver.close()
        i += 1
        break

    # time.sleep(1)
    # i += 1
    # gonext = driver.find_element_by_xpath(
    #     "/html/body/div[3]/div[2]/div/table[2]/tbody/tr/td/form/table/tbody/tr[3]/td[2]/nobr/a")
    # gonext.click()
    # time.sleep(1)
    # subject_class = driver.find_element_by_class_name("subject")
    # a_tag = subject_class.find_element_by_tag_name("a")
    # href_text = a_tag.get_attribute('herf')
    # print(href_text)


#     i += 1
#     gonext = driver.find_element_by_css_selector("")
#         "/html/body/div[3]/div[2]/div/table[2]/tbody/tr/td/form/table/tbody/tr[3]/td[2]/nobr/a")
#     gonext.click()

# subject_class = driver.find_element_by_class_name("subject")
# a_tag=subject_class.find_element_by_tag_name("a")
# href_text=a_tag.get_attribute('herf')
# print(href_text)

# links = [elem.get_attribute('href') for elem in elems]
# print(elems)
# # print(links)

# time.sleep(2)
# filedown.back()
# elems.back()
# drive.back()
# time.sleep(2)
# i += 1


# elems = driver.find_element_by_xpath(
#     "/html/body/div[3]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr["+str(i)+"]/td[2]/nobr/a")
# elems.click()

filedown.back()
elems.back()

# for number in array:
#     if number < 10:
#         continue

# /html/body/div[3]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr[11]/td[2]/nobr/a[1]
# /html/body/div[3]/div[2]/div/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/nobr/a
# /html/body/div[3]/div[2]/div/table/tbody/tr/td/div[3]/a[4]/span

# links = [elem.get_attribute('href') for elem in elems]
# print(elems)
# print(links)

# count = 1
# for image in images:
#     try:
#         image.click()
#         time.sleep(2)  # 시간차가 걸리니
#         imgUrl = driver.find_element_by_css_selector(
#             ".n3VNCb").get_attribute("src")     # 해당 class명칭 가진 이미지 많을 수 있으므로-> Copy selector/Copy XPath / Copty full XPath - by_xpath 적용
#     # python selenium image src 검색
#     # python download image by url
#     # import urllib.request
#         urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
#         count += 1
#     except:
#         pass

# driver.close()


# 'python selenium scroll down'검색

# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

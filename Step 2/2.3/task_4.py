import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver') as driver:
    driver.get('http://suninjuly.github.io/alert_accept.html')
    driver.find_element_by_tag_name('button').submit()
    driver.find_element_by_tag_name('input').send_keys(calc(int(driver.find_element_by_id('input_value').text)))
    driver.find_element_by_tag_name('button').submit()
    time.sleep(10)

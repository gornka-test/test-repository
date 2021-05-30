from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    link = "http://localhost/"
    browser = webdriver.Chrome()
    browser.get(link)
    wait = WebDriverWait(browser, 10)

    products = browser.find_elements_by_css_selector("li.product")
    for item in products:
        stickers = item.find_elements_by_css_selector('.sticker')
        assert (len(stickers) == 1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    browser.quit()


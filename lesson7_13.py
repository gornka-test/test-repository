from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

def add_to_cart(browser, link, count):
    browser.get(link)

    for i in range(count):
        browser.find_element_by_css_selector('#box-most-popular a').click()
        if browser.find_element_by_css_selector('#box-product .title').text =='Yellow Duck':
            Select(browser.find_element_by_name("options[Size]")).select_by_visible_text("Small")
        WebDriverWait(browser, 3)
        browser.find_element_by_name('add_cart_product').click()
        WebDriverWait(browser, 10).until(lambda s: int(s.find_element_by_css_selector("span.quantity").text) == i + 1)
        browser.back()

def delete_from_cart(browser):
    browser.find_element_by_css_selector('#cart').click()
    WebDriverWait(browser, 10).until(lambda s: s.find_element_by_css_selector("table.dataTable tr"))
    count = len(browser.find_elements_by_css_selector("table.dataTable tr"))
    while count > 0:
        WebDriverWait(browser, 10).until(lambda s: s.find_element_by_name('remove_cart_item'))
        browser.find_element_by_name('remove_cart_item').click()
        WebDriverWait(browser, 10).until(lambda s: len(s.find_elements_by_css_selector("table.dataTable tr")) < count)
        count = len(browser.find_elements_by_css_selector("table.dataTable tr"))
    browser.back()


link = "http://localhost/en/"
browser = webdriver.Chrome()

add_to_cart(browser, link, 3)
delete_from_cart(browser)

time.sleep(5)
browser.quit()



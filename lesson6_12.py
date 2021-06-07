from selenium import webdriver
import time
import os
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
import datetime
from selenium.webdriver.support.ui import Select




try:
    link = "http://localhost/admin/?app=catalog&doc=catalog"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()

    browser.get('http://localhost/admin/?category_id=0&app=catalog&doc=edit_product')

    def random_string(key, len):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(len)])


    WebDriverWait(browser, 3)
    browser.find_element_by_name("status").click()
    name = random_string("", 5)
    browser.find_element_by_name("name[en]").send_keys(name)
    browser.find_element_by_name("code").send_keys("1234")
    browser.find_element_by_css_selector("[value='1-1']").click()
    browser.find_element_by_name("quantity").clear()
    browser.find_element_by_name("quantity").send_keys("1")
    image = os.path.abspath(r"image.png")
    browser.find_element_by_name("new_images[]").send_keys(image)
    date_from = datetime.date.today()
    browser.find_element_by_name("date_valid_from").send_keys(date_from.strftime('%Y-%m-%d'))
    date_to = datetime.date.today() + datetime.timedelta(days=3)
    browser.find_element_by_name("date_valid_to").send_keys(date_to.strftime('%Y-%m-%d'))
    browser.find_element_by_css_selector("[href='#tab-information']").click()

    WebDriverWait(browser, 3)
    Select(browser.find_element_by_name("manufacturer_id")).select_by_visible_text("ACME Corp.")
    browser.find_element_by_name("keywords").send_keys("keywords")
    browser.find_element_by_name("short_description[en]").send_keys("Short description1")
    browser.find_element_by_css_selector(".trumbowyg-editor").send_keys("Description")
    browser.find_element_by_name("head_title[en]").send_keys("head_title")
    browser.find_element_by_name("meta_description[en]").send_keys("meta_description")
    browser.find_element_by_css_selector("[href='#tab-prices']").click()

    WebDriverWait(browser, 3)
    browser.find_element_by_name("purchase_price").clear()
    browser.find_element_by_name("purchase_price").send_keys("1")
    Select(browser.find_element_by_name("purchase_price_currency_code")).select_by_value("USD")
    browser.find_element_by_name("gross_prices[USD]").clear()
    browser.find_element_by_name("gross_prices[USD]").send_keys("10")
    browser.find_element_by_name("gross_prices[EUR]").clear()
    browser.find_element_by_name("gross_prices[EUR]").send_keys("10")
    browser.find_element_by_xpath("//button[@name='save']").click()

    browser.find_element_by_link_text(name).click()
    browser.find_element_by_name("delete").click()


finally:

    time.sleep(5)
    browser.quit()

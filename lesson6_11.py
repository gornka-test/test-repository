from selenium import webdriver
import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


try:
    link = "http://localhost/en/create_account"
    browser = webdriver.Chrome()
    browser.get(link)

    def random_string(key, len):
        symbols = string.ascii_letters + string.digits
        return "".join([random.choice(symbols) for i in range(len)])

    email = random_string("", 8) + '@test.test'
    password = random_string("", 8)

    browser.find_element_by_name('firstname').send_keys(random_string("", 10))
    browser.find_element_by_name('lastname').send_keys(random_string("", 10))
    browser.find_element_by_name('address1').send_keys('test')
    browser.find_element_by_name('postcode').send_keys('12345')
    browser.find_element_by_name('city').send_keys('test')
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('confirmed_password').send_keys(password)
    browser.find_element_by_name('phone').send_keys('+79620412066')
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_css_selector('.select2-selection__rendered').click()
    browser.find_element_by_css_selector('.select2-search__field').send_keys("United States" + Keys.ENTER)
    WebDriverWait(browser, 1)
    browser.find_element_by_name('create_account').click()

    WebDriverWait(browser, 1)
    browser.find_element_by_css_selector('#box-account li:last-of-type a').click()


    WebDriverWait(browser, 1)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('password').send_keys(password)

    WebDriverWait(browser, 1)
    browser.find_element_by_name('login').click()

    WebDriverWait(browser, 1)
    browser.find_element_by_css_selector('#box-account li:last-of-type a').click()


finally:

    time.sleep(5)
    browser.quit()

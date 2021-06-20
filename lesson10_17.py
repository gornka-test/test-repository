from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

def authorization(browser):
    link = " http://localhost/admin/?app=countries&doc=countries"
    browser.get(link)
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()
    browser.back()

def log(browser):
    for l in browser.get_log("browser"):
        print(l)

def open_window(browser):
    link = "http://localhost/admin/?app=catalog&doc=catalog&category_id=1"
    browser.get(link)
    WebDriverWait(browser, 10).until(lambda s: s.find_element_by_class_name("name"))
    list_links = browser.find_elements_by_css_selector("a[href*='product_id']")
    list_products = []
    for i in range(0, len(list_links), 2):
        href = list_links[i].get_attribute("href")
        list_products.append(href)

    # print(list_products)

    for link in range(len(list_products)):
         browser.get(list_products[link])
         WebDriverWait(browser, 10).until(lambda s: s.find_element_by_css_selector(".active"))
         log(browser)
         browser.back()

    time.sleep(5)
    browser.quit()

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

authorization(browser)
open_window(browser)







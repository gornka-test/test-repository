from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

def authorization(browser):
    link = " http://localhost/admin/?app=countries&doc=countries"
    browser.get(link)
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()
    browser.back()

def open_window(browser, wait):
    link = "http://localhost/admin/?app=countries&doc=countries"
    browser.get(link)
    browser.find_element_by_css_selector('.fa-pencil').click()

    list_external = browser.find_elements_by_css_selector('.fa-external-link')
    current_window = browser.current_window_handle
    for link in range(len(list_external)):
        list_external[link].click()
        new_window = [i for i in browser.window_handles if i != current_window]
        wait.until(EC.new_window_is_opened(new_window))

        for window in new_window:
            browser.switch_to.window(window)
            browser.close()
        browser.switch_to.window(current_window)


browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

authorization(browser)
open_window(browser, wait) 

time.sleep(5)
browser.quit()



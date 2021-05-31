from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



try:
    link = "http://localhost/admin/login.php"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()


    length_menu = len(browser.find_elements_by_css_selector("ul#box-apps-menu > li"))
    for num_menu in range(length_menu):
        menu_items = browser.find_elements_by_css_selector("ul#box-apps-menu > li")
        menu_items[num_menu].click()
        browser.implicitly_wait(10)
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # TODO: Для дебага
        time.sleep(3)

        length_child = len(browser.find_elements_by_css_selector(".docs>li>a"))
        for num_submenu in range(length_child):
            submenu_items = browser.find_elements_by_css_selector(".docs>li>a")
            submenu_items[num_submenu].click()
            heading = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    browser.quit()


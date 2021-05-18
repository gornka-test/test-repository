from selenium import webdriver
import time


try:
    link = "https://github.com/gornka-test/test-repository"
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
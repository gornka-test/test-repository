from selenium import webdriver
import time

try:
    link = "http://localhost/admin/login.php"
    browser = webdriver.Chrome()
    browser.get(link)


finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(3)
        # закрываем браузер после всех манипуляций
     browser.quit()
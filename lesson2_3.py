from selenium import webdriver
import time

try:
    link = "http://localhost/admin/login.php"
    browser = webdriver.Chrome()
    browser.get(link)

    username = browser.find_element_by_name("username")
    username.send_keys("admin")

    password = browser.find_element_by_name("password")
    password.send_keys("admin")

    # Отправляем заполненную форму
    buttonLogin = browser.find_element_by_name("login")
    buttonLogin.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(3)
        # закрываем браузер после всех манипуляций
     browser.quit()

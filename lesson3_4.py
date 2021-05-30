from selenium import webdriver
import time

try:
    link = "http://localhost/admin/login.php"
    #chrome_driver = webdriver.Chrome()
    firefox_driver = webdriver.Firefox(executable_path='/Users/karinagorn/geckodriver')
    #browser.get(link)
    firefox_driver.get(link)

    username = firefox_driver.find_element_by_name("username")
    username.send_keys("admin")

    password = firefox_driver.find_element_by_name("password")
    password.send_keys("admin")

    # Отправляем заполненную форму
    buttonLogin = firefox_driver.find_element_by_name("login")
    buttonLogin.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(3)
        # закрываем браузер после всех манипуляций
     firefox_driver.quit()
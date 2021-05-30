from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

try:
    link1 = 'http://localhost/admin/?app=countries&doc=countries'
    link2 = 'http://localhost/admin/?app=geo_zones&doc=geo_zones'
    browser = webdriver.Chrome()

    browser.get(link1)
    browser.find_element_by_name("username").send_keys("admin")
    browser.find_element_by_name("password").send_keys("admin")
    browser.find_element_by_name("login").click()
    wait = WebDriverWait(browser, 10)

    listCountries = []
    countries = browser.find_elements_by_css_selector('tr.row a:not([title])')
    for country in range(len(countries)):
        listCountries.append(countries[country].get_attribute('textContent'))
    assert (listCountries == sorted(listCountries))

    zone = browser.find_elements_by_css_selector('td:nth-child(6)')


    for element in range(len(zone)):
        browser.implicitly_wait(2)
        if zone[element].text != '0':
            zone1 = browser.find_elements_by_css_selector('td:nth-child(5)>a')
            zone1[element].click()

            zones = browser.find_elements_by_css_selector("#table-zones tr>td:nth-child(3) [type=hidden]")
            listZones = []
            for elementZone in range(len(zones)):
                listZones.append(zones[elementZone].get_attribute('textContent'))
                assert (listZones == sorted(listZones))
                browser.back()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    browser.quit()


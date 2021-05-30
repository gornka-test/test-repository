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

    listZones = [i.text for i in browser.find_elements_by_css_selector("td:nth-child(6)")]
    indexZones = [listZones.index(i) for i in listZones if i != '0']

    for zoneZero in indexZones:
        country = browser.find_elements_by_css_selector("td:nth-child(5)>a")
        country[zoneZero].click()
        zones = [i.get_attribute("textContent") for i in
                 browser.find_elements_by_css_selector("#table-zones tr>td:nth-child(3)") if
                 i.get_attribute("textContent") != ""]
        assert (zones == sorted(zones))
        browser.back()

    browser.get(link2)
    browser.implicitly_wait(10)

    zones_number = len(browser.find_elements_by_css_selector("tr.row"))

    while zones_number:
        zones_number -= 1
        country = browser.find_elements_by_css_selector("td:nth-child(3)>a")
        country[zones_number].click()
        zones = [i.get_attribute("textContent") for i in
                 browser.find_elements_by_css_selector("td:nth-child(3)>select option[selected]")]
        assert (zones == sorted(zones))
        browser.back()


finally:
    time.sleep(3)
    browser.quit()


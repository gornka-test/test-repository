from selenium import webdriver
import time
from selenium.webdriver.support.color import Color

try:
    link = "http://localhost"
    browser = webdriver.Chrome()
    browser.get(link)

    #элементы главной страницы
    name_main = browser.find_element_by_css_selector("#box-campaigns .name")
    name_main_text = name_main.text

    regular_main = browser.find_element_by_css_selector('#box-campaigns s.regular-price')
    regular_main_text = regular_main.text
    regular_main_size = float(regular_main.value_of_css_property('font-size')[0:-2])
    color_regular_main = regular_main.value_of_css_property("color")

    campaign_main = browser.find_element_by_css_selector('#box-campaigns strong.campaign-price')
    campaign_main_text = campaign_main.text
    campaign_main_size = float(campaign_main.value_of_css_property('font-size')[0:-2])
    color_campaign_main = campaign_main.value_of_css_property("color")

    browser.find_element_by_css_selector("#box-campaigns a").click()
    browser.implicitly_wait(10)

    # элементы страницы товара
    name_page = browser.find_element_by_css_selector('#box-product .title')
    name_page_text = name_page.text

    regular_page = browser.find_element_by_css_selector('#box-product .regular-price')
    regular_page_text = regular_page.text
    regular_page_size = float(regular_page.value_of_css_property('font-size')[0:-2])
    color_regular_page = regular_page.value_of_css_property("color")

    campaign_page = browser.find_element_by_css_selector('#box-product .campaign-price')
    campaign_page_text = campaign_page.text
    campaign_page_size = float(campaign_page.value_of_css_property('font-size')[0:-2])
    color_campaign_page = campaign_page.value_of_css_property("color")

    #проверка 1 - на главной странице и на странице товара совпадает текст названия товара
    assert (name_main_text == name_page_text)
    #проверка 2 - на главной странице и на странице товара совпадают цены (обычная и акционная)
    assert (campaign_main_text == campaign_page_text)
    assert (regular_main_text == regular_page_text)

    # проверка 3 - обычная цена зачёркнутая и серая (проверка на зачеркнутость уже есть в селекторе)
    r_main_color = Color.from_string(color_regular_main).red
    g_main_color = Color.from_string(color_regular_main).blue
    b_main_color = Color.from_string(color_regular_main).green
    assert (r_main_color == g_main_color == b_main_color)

    r_page_color = Color.from_string(color_regular_page).red
    g_page_color = Color.from_string(color_regular_page).blue
    b_page_color = Color.from_string(color_regular_page).green
    assert (r_page_color == g_page_color == b_page_color)

    # проверка 4 - акционная цена жирная и красная
    g_page_color_campaign = Color.from_string(color_campaign_page).green
    b_page_color_campaign = Color.from_string(color_campaign_page).blue
    assert (g_page_color_campaign == b_page_color_campaign == 0)

    g_main_color_campaign = Color.from_string(color_campaign_main).green
    b_main_color_campaign = Color.from_string(color_campaign_main).blue
    assert (g_main_color_campaign == b_main_color_campaign == 0)

    # проверка 5 - акционная цена крупнее, чем обычная
    assert(regular_main_size < campaign_main_size)
    assert(regular_page_size < campaign_page_size)


finally:

    time.sleep(1)
    browser.quit()

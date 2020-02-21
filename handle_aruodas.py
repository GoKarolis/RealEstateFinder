import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")


def open_aruodas():
    driver.get(
        "https://www.aruodas.lt/sklypai-pardavimui/vilniaus-rajone/?FOfferType=1"
    )
    driver.maximize_window()


def adjust_choices(min_price, max_price, min_size, max_size):
    elem = driver.find_element_by_id("input_FPriceMin")
    elem.send_keys(min_price)
    time.sleep(1)
    elem = driver.find_element_by_id("input_FPriceMax")
    elem.send_keys(max_price)
    time.sleep(1)
    elem = driver.find_element_by_id("input_FAreaOverAllMin")
    elem.send_keys(min_size)
    time.sleep(1)
    elem = driver.find_element_by_id("input_FAreaOverAllMax")
    elem.send_keys(max_size)
    time.sleep(1)
    elem = driver.find_element_by_id("buttonSearchForm")
    elem.click()
    time.sleep(3)
    select = Select(driver.find_element_by_id("changeListOrder"))
    select.select_by_value("Price")
    time.sleep(3)


def get_best_offers():
    best_aruodas_offers = {}
    time.sleep(3)
    items_element = driver.find_elements_by_class_name("list-row")
    items_found = []
    for x in items_element:
        items_found.append(x.text)
    counter = 4
    rating = 0
    select = Select(driver.find_element_by_id("changeListOrder"))
    select.select_by_value("Price")
    time.sleep(3)
    for x in items_found:
        counter -= 1
        rating += 1
        if counter > 0:
            x.strip()
            if x != "":
                x = x[1:]
                x.strip()
                best_aruodas_offers["#" + str(rating)] = x
            else:
                continue
    return best_aruodas_offers


def get_json():
    with open("aruodas_data.txt", "r") as json_file:
        data = json.load(json_file)
    offer_one = data["#1"]
    offer_two = data["#2"]
    offer_three = data["#3"]
    return offer_one, offer_two, offer_three


def close_browser():
    driver.quit()

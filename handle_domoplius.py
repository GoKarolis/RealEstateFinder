import time
from selenium import webdriver
import json


driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")


def open_domo():
    driver.get("https://domoplius.lt/skelbimai/sklypai?action_type=1&address_1=462")
    driver.maximize_window()


def adjust_choices(min_price, max_price, min_size, max_size):
    elem = driver.find_element_by_name("sell_price_from")
    elem.send_keys(min_price)
    time.sleep(1)
    elem = driver.find_element_by_name("sell_price_to")
    elem.send_keys(max_price)
    time.sleep(1)
    elem = driver.find_element_by_name("site_size_from")
    elem.send_keys(min_size)
    time.sleep(1)
    elem = driver.find_element_by_name("site_size_to")
    elem.send_keys(max_size)
    time.sleep(1)
    elem = driver.find_element_by_class_name("ico-search")
    elem.click()
    time.sleep(3)


def get_best_offers():
    best_domo_offers = {}
    time.sleep(3)
    items_element = driver.find_elements_by_class_name("not-viewed")
    items_found = []
    for x in items_element:
        items_found.append(x.text)
    counter = 4
    rating = 0
    for x in items_found:
        if "+" not in x:
            counter -= 1
            rating += 1
            if counter > 0:
                best_domo_offers["#" + str(rating)] = x
    return best_domo_offers


def get_json():
    with open("domo_data.txt", "r") as json_file:
        data = json.load(json_file)
    offer_one = data["#1"]
    offer_two = data["#2"]
    offer_three = data["#3"]
    return offer_one, offer_two, offer_three


def close_browser():
    driver.quit()

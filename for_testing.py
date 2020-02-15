import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")
driver.get("https://www.aruodas.lt/sklypai-pardavimui/?FOfferType=1&FAreaOverAllMin=0&FPriceMin=10000&FPriceMax=50000&FAreaOverAllMax=500")

def get_best_offers():
    time.sleep(3)
    items_element = driver.find_elements_by_class_name("list-row")
    items_found = []
    for x in items_element:
        items_found.append(x.text)

    # -------------- Get 3 best offers --------------

    counter = 4
    select = Select(driver.find_element_by_id("changeListOrder"))
    select.select_by_value("Price")
    time.sleep(3)
    for x in items_found:
        counter -= 1
        if counter > 0:
            x.strip()
            if x != "":
                x = x[1:]
                x.strip()
                print(x)
            else:
                continue
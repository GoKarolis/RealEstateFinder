from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.set_page_load_timeout(15)
driver.get("https://aruodas.lt/")
driver.find_element_by_class_name("btn submit_frm").click()
time.sleep(3)
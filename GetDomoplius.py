from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.set_page_load_timeout(15)
driver.get("https://domoplius.lt/")
driver.find_element_by_class_name("btn submit_frm").click()
time.sleep(3)

import time
from selenium import webdriver

driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
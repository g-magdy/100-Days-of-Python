from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable-logging'])

driver = webdriver.Chrome(options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python"+Keys.ENTER)
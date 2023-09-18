from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Tom")
lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Jerry")
email = driver.find_element(By.NAME, "email")
email.send_keys("myemail@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()
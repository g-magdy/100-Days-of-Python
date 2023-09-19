import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items.pop()
items_ids = [item.get_attribute("id") for item in items]

# print(items_ids)

start = time.time()
check = start + 10
# 5 minutes
stop = start + 60*5
while time.time() < stop:
    cookie.click()

    # every 5 seconds
    if time.time() > check:
        #get <b> tags
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices.pop()
        prices = [int(price.text.split('-')[1].strip().replace(',', '')) for price in prices]
        
        owned = int(money.text.replace(',', ''))
        for price in prices[::-1]:
            if owned > price:
                i = prices.index(price)
                try:
                    up = driver.find_element(By.ID, items_ids[i])
                    time.sleep(0.1)
                    up.click()
                    check = time.time() + 10
                    break
                except StaleElementReferenceException:
                    pass
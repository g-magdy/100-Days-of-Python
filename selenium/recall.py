# I regret every single day I have not practived coding!
# I can now see how easy it is to become a computer engineer
# I can beat procrastination, just start when you are not ready.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
start = time.time()
# make the window not disappear
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("detach", True)

# REMOVE THE ANNOYING CONSOLE MESSAGE
options.add_experimental_option("excludeSwitches", ['enable-logging'])
# start the driver
driver = webdriver.Chrome(options)
# GET THE WEBSITE
driver.get("https://en.wikipedia.org/wiki/Main_Page")
n_of_articlies = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
n_of_articlies.click
print(n_of_articlies.text.replace(',', ''))

# close the driver
driver.quit()
end = time.time()
print(f"Time of execution is {end - start} sec")
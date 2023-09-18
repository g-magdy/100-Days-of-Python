from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) 
driver = webdriver.Chrome(options)
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
article_count = int(article_count.text.replace(',', ''))
print(article_count)

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
# for the browser tab not to close itself once finished loading
options.add_experimental_option("detach", True)
# create the driver
driver = webdriver.Chrome(options=options)
# search for a specific web-page
# url = "https://www.amazon.eg/-/en/gp/product/B0BNK17BH2/ref=ox_sc_act_title_2?smid=A3M0W4261CSGPO&psc=1"
url = "https://python.org"
driver.get(url)

# finding elements by class name
# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole") 
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("id"))
css_selector = ".documentation-widget p a"
css_selector_2 = "#content > div > section > div:nth-child(1) > div.small-widget.documentation-widget > p:nth-child(3) > a"

docs_link = driver.find_element(By.CSS_SELECTOR, value=css_selector)
print(docs_link.text)

# close all tabs 
driver.quit()

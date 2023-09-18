from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://python.org"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get(url)
events = {}
lis = driver.find_elements(By.CSS_SELECTOR, "#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li")
for index, l in enumerate(lis):
    events[index] = {
        "time": l.find_element(By.TAG_NAME, "time").get_attribute("datetime").split('T')[0], #type: ignore
        "name": l.find_element(By.TAG_NAME, "a").text
    }

print(events)
driver.quit()
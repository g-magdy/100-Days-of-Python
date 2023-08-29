from bs4 import BeautifulSoup
import requests

print("Welcome to the musical time machine")
date = input("Which date do you want to travel to ?\nType the date in the format of YYYY-MM-DD\n")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/")
response.raise_for_status()
soup = BeautifulSoup(markup=response.text, features="html.parser")
h3s = soup.select(selector="ul li ul li h3")
h3s = [(h3.text).strip() for h3 in h3s]    
print(h3s)
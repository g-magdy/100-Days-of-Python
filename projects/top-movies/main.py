#Here, I'll use web-scraping to make a text file of 
# the names of these 100 movies #
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2")
soup = BeautifulSoup(markup=response.text, features="html.parser")

titles = soup.select(selector="h3.title")
titles = [title.text.replace(')', '-') for title in titles]
titles.reverse()
with open (file="movies.txt", mode="w", encoding="utf8") as file:
    for title in titles:
        file.write(f"{title}\n")
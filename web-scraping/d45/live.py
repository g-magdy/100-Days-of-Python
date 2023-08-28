from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/")
# response.text is the source code of the live website
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# titlelines = soup.select(selector="td.title span.titleline a")
links = []
texts = []
points = []
titles = soup.select(selector="td.title span.titleline a")
for t in titles:
    l = t.attrs["href"]
    if l[0:5] != "from?":
        links.append(l)
        texts.append(t.get_text())
    

scores = soup.select(selector="td.subtext span.subline .score")
for score in scores:
    points.append(int(score.get_text().split()[0]))

print(len(links))
print(len(texts))
print(len(points))
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

articles = []
for l, t, p in zip(links, texts, points):
    articles.append({
        "text": t,
        "link": l,
        "points":p
    })

# index_of_max = 0
# for index, article in enumerate(articles):
#     if article["points"] > articles[index_of_max]["points"]:
#         index_of_max = index
        
# print(articles[index_of_max])

print(articles[points.index(max(points))])

# remember to check https://<page>/robots.txt 
# to see what is allowed and what is not allowed to scrape
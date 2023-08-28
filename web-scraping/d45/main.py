from bs4 import BeautifulSoup
with open(file="website.html", mode="r", encoding="utf8") as file:
    content = file.read()
    
soup = BeautifulSoup(content,"html.parser")

all_anchor = soup.find_all(name='a')
# for tag in all_anchor:
#     # print(tag.text)
#     print(tag.get("href"))
    

print(soup.find(id="name"))
print(soup.find(name="h3", class_="heading"))
# the  string is a CSS selector
print(soup.select_one(selector="p a").get("href")) #type: ignore

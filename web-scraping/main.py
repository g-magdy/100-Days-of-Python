from bs4 import BeautifulSoup
with open(file="website.html", mode="r", encoding="utf8") as file:
    content = file.read()
    
soup = BeautifulSoup(content,"html.parser")

all_anchor = soup.find_all(name='a')
print(all_anchor)
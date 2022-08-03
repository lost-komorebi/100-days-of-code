from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(r.text, 'html.parser')

titles = soup.find_all(name='a', class_="titlelink")
scores = soup.find_all(name='span', class_="score")

links = [i.get('href') for i in titles]
titles = [i.text for i in titles]
scores = [int(i.text.split(" ")[0]) for i in scores]

for x, y, z in sorted(zip(titles, links, scores),
                      key=lambda i: i[2], reverse=True):
    # order by score desc
    print(x, y, z)

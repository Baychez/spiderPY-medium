from bs4 import BeautifulSoup as bs4
import requests
import sys 
import re

page = requests.get("https://medium.com")

body = bs4(page.text, "html.parser")
links = {a['href'] for a in body.find_all("a")}
try:
    for r in range(int(sys.argv[1])):
        for i in links.copy():
            try: 
                for j in bs4(requests.get(i).content, 'lxml').find_all("a"):
                    links.add(j['href'])
            except: 
                pass
except: 
    pass
with open('storys.txt', 'w') as s:
    for i in links: 
        if re.search(r'\-+\d+\-+\d+\-+', i):
            s.write(i + '\n')
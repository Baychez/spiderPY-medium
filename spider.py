from bs4 import BeautifulSoup as bs4
import requests
import sys 
import re

try: 
    page = requests.get(sys.argv[1])
except IndexError:
    page = requests.get("https://medium.com")

body = bs4(page.content, "html.parser")
links = {a['href'] for a in body.find_all("a")}

for i in links:
    print(i)
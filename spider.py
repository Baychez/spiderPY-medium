import numpy
from bs4 import BeautifulSoup as bs4
import requests
import sys 

try: 
    page = requests.get(sys.argv[1])
except IndexError:
     page = requests.get("https://medium.com")

body = bs4(page.content, "html.parser")
print(len(body.find_all("script")))
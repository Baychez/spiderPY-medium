from bs4 import BeautifulSoup as bs4
import requests
import sys 
import re

page = requests.get("https://medium.com")

body = bs4(page.text, "html.parser")
links = {a['href'] for a in body.find_all("a")}
old_links = []
try:
	for r in range(int(sys.argv[1])):
		for i in links.copy():
			if i not in old_links and re.match('http', i):
				old_links.append(i)
				for j in bs4(requests.get(i).content, 'lxml').find_all("a"):
					try:
						links.add(j['href'])
					except KeyError:
						pass
			else:
				print(i)
except IndexError: 
	pass

	
with open('links.txt', 'w') as s:
	for i in links: 
		s.write(i + '\n')
with open('storys.txt', 'w') as s:
	for i in links: 
		if re.search(r'\-+\d+\-+\d+\-+', i):
			s.write(i + '\n')
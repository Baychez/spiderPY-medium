from bs4 import BeautifulSoup as bs4
import requests
import sys 
import re
url = "https://medium.com"
page = requests.get(url)

body = bs4(page.text, "html.parser")
links = {a['href'] for a in body.find_all("a")}
old_links = []
def add_and_search(x):
	old_links.append(x)
	for j in bs4(requests.get(x).content, 'lxml').find_all("a"):
		try:
			links.add(j['href'])
		except KeyError:
			pass
try:
	looper = int(sys.argv[1]) if len(sys.argv) > 1 else 1
except ValueError:
	print("Third argument must be a number")
	quit()

for r in range(looper):
	for i in links.copy():
		if i not in old_links:
			if re.match('http', i):
				add_and_search(i)
			elif re.match('/[^/]', i):
				add_and_search(f"{url}{i}")	
		else:
			print(i)


	
with open('links.txt', 'w') as s:
	s.write(f"from {looper} loops of mediums urls")
	for i in links: 
		s.write(i + '\n')
with open('storys.txt', 'w') as s:
	s.write(f"from {looper} loops of mediums urls")
	for i in links: 
		if re.search(r'\-+\d+\-+\d+\-+', i):
			s.write(i + '\n')
from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/List_of_Running_Man_episodes_(2020)')

soup = BeautifulSoup(r.text, "html.parser")
span = soup.find("span", id="Episodes")
table = span.parent.find_next_sibling("table")
table_rows = table.tbody.find_all('tr')

f = open("running_man_episodes_2020.txt","w+")

for index, row in enumerate(table_rows):
	if index == 0: 
		continue
	else:
		th = row.find_all('th')[-1]
		f.write(th.text)

f.close()
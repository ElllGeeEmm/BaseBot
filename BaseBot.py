from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome', headless=True)
url = 'http://www.espn.com/mlb/scoreboard'

browser.visit(url)
content = browser.html
soup = BeautifulSoup(content, 'lxml')

games = soup.findAll('article', {'class':'scoreboard'})

for i in range(len(games)):
	away = games[i].find('tr', {'class': 'away'}).find('span', {'class': 'sb-team-short'})
	home = games[i].find('tr', {'class': 'home'}).find('span', {'class': 'sb-team-short'})
	time = games[i].find('span', {'class': 'time'})
	print ("{}@{} {}".format(away.text, home.text, time.text))


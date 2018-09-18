from splinter import Browser
import datetime
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, Game
import settings

browser = Browser('chrome', headless=True)
url = 'http://www.espn.com/mlb/scoreboard'

#database linking
engine = create_engine('sqlite:///games.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

games_db = session.query(Game).filter(Game.date == datetime.date.today()).all()

while games_db == []:

	browser.visit(url)
	content = browser.html
	soup = BeautifulSoup(content, 'lxml')

	games = soup.findAll('article', {'class':'scoreboard'})



	for i in range(len(games)):
		away = games[i].find('tr', {'class': 'away'}).find('span', {'class': 'sb-team-short'})
		home = games[i].find('tr', {'class': 'home'}).find('span', {'class': 'sb-team-short'})
		time = games[i].find('span', {'class': 'time'})
		new_game = Game(date=datetime.date.today(), time=time.text, away_team=away.text, home_team=home.text)
		session.add(new_game)
	
		print ("{}@{} {}".format(away.text, home.text, time.text))
	

	session.commit()
	games_db = session.query(Game).filter(Game.date == datetime.date.today()).all()

for game in games_db:
	print ("{}@{} {}".format(game.away_team, game.home_team, game.time))
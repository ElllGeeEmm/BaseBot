from splinter import Browser
import datetime
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, Game
from settings import *
import praw

browser = Browser('chrome', headless=True)
url = 'http://www.espn.com/mlb/scoreboard'

#database linking
engine = create_engine('sqlite:///games.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def get_todays_games():

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
			print ("{}@{} {}".format(away.text, home.text, time.text))
			new_game = Game(date=datetime.date.today(), time=time.text, away_team=away.text, home_team=home.text)
			session.add(new_game)
				
		session.commit()
		session.close()
		
		games_db = session.query(Game).filter(Game.date == datetime.date.today()).all()
	return games_db

games_db = get_todays_games()

reddit = praw.Reddit(client_id = reddit_client_id,
					 client_secret = reddit_client_secret,
					 password = reddit_password,
					 user_agent = 'script in testing by u/ElllGeeEmm',
					 username = reddit_username)

def post_pregame_threads(games_db):
	for game in games_db:
		if game.pregame_URL is None:
			submission = reddit.subreddit("PostHereAndIllBanYou").submit(title = "Pre-Game Thread: {}@{} {}".format(game.away_team, game.home_team, game.time),
																	 selftext = "{}@{} {}".format(game.away_team, game.home_team, game.time))
			game.pregame_URL = submission.permalink
			session.add(game)
		else:
			print ("Pre-Game thread posted: {}@{} {}".format(game.away_team, game.home_team, game.time))

post_pregame_threads(games_db)
			
session.commit()
session.close()
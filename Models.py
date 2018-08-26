import os
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Game(Base):
	__tablename__ = 'game'
	
	id = Column(Integer, primary_key=True)
	date = Column(String, nullable=False)
	time = Column(String)
	away_team = Column(String, nullable=False)
	away_roster = Column(String)
	home_team = Column(String, nullable=False)
	home_roster = Column(String)
	pregame_URL = Column(String)
	gametime_URL = Column(String)
	postgame_URL = Column(String)
	
	#def __repr__(self):
	#	return "<Game: {}@{} {}>".format(Game.away_team, Game.home_team, Game.date_time)

engine = create_engine('sqlite:///games.db')

Base.metadata.create_all(engine)
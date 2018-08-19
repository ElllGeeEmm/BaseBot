from bs4 import BeautifulSoup
import requests, os

ESPN_gameday_url = "http://www.espn.com/mlb/scoreboard"
raw_gameday_data = requests.get(ESPN_gameday_url)

print (raw_gameday_data.status_code)
print (raw_gameday_data.encoding)

soup = BeautifulSoup(raw_gameday_data.text, 'html.parser')

games = soup.find_all('article')

print (len(games))


#game_div = soup.find('div', attrs={'id': 'events'})
#games = game_div.find_all('article')

#print (game_div.id)

#os.remove("raw.txt")
#f=open("soup.txt",'w+')
#f.write(soup.text)
#f.close


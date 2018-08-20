from bs4 import BeautifulSoup
import requests, os

ESPN_gameday_url = "http://www.espn.com/mlb/scoreboard"
raw_gameday_data = requests.get(ESPN_gameday_url)

print (raw_gameday_data.status_code)
print (raw_gameday_data.encoding)

soup = BeautifulSoup(raw_gameday_data.content, 'html.parser')

print(soup.find_all("article", attrs={"class": "scoreboard"}))
#print(len(games))
#print(games[0])


#game_div = soup.find('div', attrs={'id': 'events'})
#games = game_div.find_all('article')

#print (game_div.id)

#os.remove("raw.txt")
#f=open("soup.txt",'w+')
#f.write(soup.text)
#f.close


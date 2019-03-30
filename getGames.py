import requests
import json
import collections

seasons = ["2008","2009",'2010']

for season in seasons:
	for teamId in range(1,31):
		url = f"https://www.balldontlie.io/api/v1/stats?seasons[]={season}&team_ids[]={teamId}&per_page=120"
		resp = requests.get(url=url)
        games = resp.json()

        dates = []
        for game in games['data']:
        	dates.append(game['date'][:10])
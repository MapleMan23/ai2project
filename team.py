import requests 
import numpy as np
import player as p

class Team():
	def __init__(self, teamID, season):
		self.id = teamID
		self.season = season
		self.schedule = self.getScheduleDates()
		self.roster = self.createRoster()

	def createRoster(self):
		with open(f"roster.json") as f:
			roster = []
			team = json.load(f)[self.season][str(self.id)]
			for member in team:
				roster.append(p.Player(member['id'], self.season, self.schedule))

			return np.array(roster)

	def getScheduleDates(self):
		url = f"https://www.balldontlie.io/api/v1/stats?seasons[]={self.season}&team_ids[]={self.id}&per_page=120"
		resp = requests.get(url=url)
        games = resp.json()

        dates = sorted([game['date'][:10] for game in games['data']])
        return np.array(dates)
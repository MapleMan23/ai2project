import requests 
import numpy as np
import player as p
import json

class Team():
	def __init__(self, teamID, season):
		self.id = str(teamID)
		self.season = str(season)
		self.schedule = self.getScheduleDates()
		self.roster = self.createRoster()

	def createRoster(self):
		with open("data/roster.json") as f:
			roster = []
			team = json.load(f)[self.season][0][str(self.id)]
			for member in team:
				roster.append(p.Player(member['id'], self.season, self.schedule))

			return np.array(sorted(roster, key=lambda x: x.avgMins, reverse=True)[:12])

	def getScheduleDates(self):
		url = f"https://www.balldontlie.io/api/v1/games?seasons[]={self.season}&team_ids[]={self.id}&per_page=120"
		resp = requests.get(url=url)
		games = resp.json()

		dates = sorted([game['date'][:10] for game in games['data']])
		return np.array(dates)

	def getGameNum(self, gameDate):
		gameNum = None
		for i, date in enumerate(self.schedule):
			if date == gameDate:
				gameNum = i
				break

		if gameNum is None:
			print(gameDate, self.id)

		return gameNum
	def getStats(self, date):
		gameNum = self.getGameNum(date)

		stats = []
		for player in self.roster:
			stats.append(player.getStats(gameNum))

		return np.array(stats).flatten()
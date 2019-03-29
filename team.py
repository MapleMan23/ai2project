import requests 
import numpy as np
import player as p

class Team():
	def __init__(self, teamID, season):
		self.id = teamID
		self.roster = createRoster(season)

	def createRoster(self, season):
		roster = []
		with open(f"roster.json") as f:
			team = json.load(f)[season][str(self.id)]
			for member in team:
				roster.append(p.Player(member['id']))

		return np.array(roster)
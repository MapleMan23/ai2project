import player
import team
import json
import time
import numpy as np

now = time.time()
teams = []
for id in range(1,2):
	teams.append(team.Team(id, 2008))
# print(time.time() - now)

dtype = [('date', '|S10'), ('home', int), ('visitor', int), ('homeWin', int)]
games = []
with open('data/2008GameResults.csv') as f:
	for line in f:
		date, home, visitor, homeWin = line.split(',')
		# if game[0] == 'Date':
		# 	break
		# print(str(date))
		games.append((date, int(home), int(visitor), int(homeWin)))
		# print(games[-1])

games = np.sort(np.array(games, dtype=dtype), order=['date', 'home', 'visitor'])


# print(games[homeGames + awayGames]['date'])
# print(allGames)
# print(teams)
train = []
gamesProccessed = []
for team in teams:
	teamid = int(team.id)
	homeGames = games['home'] == teamid 
	awayGames = games['visitor'] == teamid
	allGames = np.sort(games[homeGames + awayGames], order='date')

	for game in allGames:
		if game in gamesProccessed:
			break
		else:
			gamesProccessed.append(game)

		gameDate = game['date'].decode('utf-8')
		homeTeam = teams[0]#int(game['home'])-1]
		awayTeam = teams[0]#int(game['visitor'])-1]

		homePlayers = homeTeam.getStats(gameDate)
		awayPlayers = awayTeam.getStats(gameDate)

		row = np.concatenate(([gameDate], homePlayers, awayPlayers, [str(game['homeWin'])]))
		train.append(row)

train = np.array(train)

# print(train)
with open('train.csv', 'w') as f:
	# np.savetxt(f, train, delimiter=',')
	for row in train:
		f.write(','.join(row))
		f.write('\n')
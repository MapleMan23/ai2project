import player
import team
import json
<<<<<<< HEAD
import time

# t1 = team.Team(2, 2008)
# p1 = player.Player(971, "2008", t1.schedule)
# # print(t1.roster)
# for p in t1.roster:
# 	print(p.avgMins)

now = time.time()
teams = []
for id in range(1,31):
	teams.append(team.Team(id, 2008))
print(time.time() - now)

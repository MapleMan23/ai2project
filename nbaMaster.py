import player as p
import json
def fuckWithTheData():
	pass

p1 = p.Player(145)
data = p1.getSeasonData(2017)

gameNum = 45
for gameNum in range(1,50):
	stats = []
	stats.append(data['data'][gameNum]['player']['last_name'])
	stats.append(data['data'][gameNum]['pts'])
	stats.append(data['data'][gameNum]['reb'])
	stats.append(data['data'][gameNum]['ast'])
	stats.append(data['data'][gameNum]['blk'])
	stats.append(data['data'][gameNum]['min'])
	print(stats)
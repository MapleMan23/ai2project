import player
import team
import json

t1 = team.Team(2, 2008)
p1 = player.Player(971, "2008", t1.schedule)
print(p1.data)

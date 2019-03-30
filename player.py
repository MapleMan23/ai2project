import json
import numpy as np

class Player():
    def __init__(self, playerID, season, schedule):
        self.id = str(playerID)
        self.data = self.getData(season, schedule)

    def getData(self, season, schedule):
        stats = ['ast','blk','dreb','oreb','min','pts','stl','turnover']
        with open(f"{season}StatsWithDates.json") as f:
            seasonData = json.load(f)[self.id][0]
            data = {k:[] for k in stats}
            for date in schedule:
                try:
                    gameStats = seasonData[game]
                    for k,v in gameStats.items():
                        val = v
                        if k == 'min':
                            m = v.split(':') 
                            val = int(m[0]) + int(m[1]) / 60
                        data[k].append(float(val))
                except:
                    for k in stats:
                        data[k].append(0.0)

            return np.array([v for v in data.values()])

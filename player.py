import json
import numpy as np

class Player():
    def __init__(self, playerID, season, schedule):
        self.id = str(playerID)
        self.stats = self.getData(season, schedule)
        self.avgMins = np.mean(self.stats[4])

    def getData(self, season, schedule):
        stats = ['ast','blk','dreb','oreb','min','pts','stl','turnover']
        with open(f"data/{season}StatsWithDates.json") as f:
            seasonData = json.load(f)[self.id][0]
            data = {k:[] for k in stats}
            for date in schedule:
                try:
                    gameStats = seasonData[date]
                    for k,v in gameStats.items():
                        val = v
                        if k == 'min':
                            m = v.split(':') 
                            val = int(m[0]) + int(m[1]) / 60
                        data[k].append(float(val))
                except:
                    for k in stats:
                        data[k].append(0.0)

            return np.array([np.array(v) for v in data.values()])


    def getStats(self, gameIndex):
        stats = []
        for stat in self.stats:
            # if gameIndex == 0:
            #     stats.append(0)
            # else:
            stats.append(np.mean(stat[:gameIndex+1]))

        return np.array(stats)
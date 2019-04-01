import requests
import json
import collections

# https://www.balldontlie.io/api/v1/stats?start_date=2010-10-1&end_date=2010-10-31&per_page=15000

# for i in range(1,3093):
#     url = f"https://www.balldontlie.io/api/v1/players/{i}"
#     resp = requests.get(url=url,params=params)
#     jsonResp = resp.json

playerStats = {}
seasons = ["2011"]
stats = ['ast','blk','dreb','oreb','min','pts','stl','turnover']

f = open('roster.json')
roster = json.load(f)
f.close()

for season in roster:
    # print(season)
    seasonStats = {}
    for teams in roster[season]:
        # print(teams)
        for team in teams:
            print(team)
            for player in teams[team]:
                print(player)
                url = f"https://www.balldontlie.io/api/v1/stats?seasons[]={season}&player_ids[]={player['id']}&per_page=120"
                resp = requests.get(url=url)
                games = resp.json()
                dates = []
                gameStats = {}
                for game in games['data']:
                    gameId = game['game']['date'][:10]
                    dates.append(gameId)
                    ps = {}
                    for s in stats:
                        v = game[s]
                        ps[s] = v if v is not None else 0

                    gameStats[gameId] = ps

                # playerStats = {s:[] for s in stats}
                # gameStats = collections.OrderedDict(gameStats.items())
                # print(gameStats.keys())

                # print(sorted(dates))

                # for d in sorted(dates):
                #     for k, v in gameStats[d].items():
                #         playerStats[k].append(v)

                seasonStats[player['id']] = [gameStats]

    with open(f'{season}StatsWithDates.json','w') as outfile:
        json.dump(seasonStats,outfile,indent=1)

    print(f'done with season {season}')
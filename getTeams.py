import requests
import json

# https://www.balldontlie.io/api/v1/stats?start_date=2010-10-1&end_date=2010-10-31&per_page=15000

# for i in range(1,3093):
#     url = f"https://www.balldontlie.io/api/v1/players/{i}"
#     resp = requests.get(url=url,params=params)
#     jsonResp = resp.json

seasonRosters = {}
for season in ["2008", "2009", "2010"]:
    url = f"https://www.balldontlie.io/api/v1/stats"
    params = dict(
        start_date=f"{season}-10-01",
        end_date=f"{season}-11-15",
        per_page='1500'
    )
    resp = requests.get(url=url,params=params)
    games = resp.json()
    # print(games)

    teamRoster = {} 

    for game in games['data']:
        teamId = game['team']['id']
        if teamId not in teamRoster.keys():
            teamRoster[teamId] = []
        player = {   
                'id': game['player']['id'],
                'first': game['player']['first_name'],
                'last': game['player']['last_name']
                }
        if player not in teamRoster[teamId]:
            teamRoster[teamId].append(player)

    seasonRosters[season] = [teamRoster]

with open('roster.json','w') as outfile:
    json.dump(seasonRosters,outfile,indent=2)
import requests
import json

# https://www.balldontlie.io/api/v1/stats?start_date=2010-10-1&end_date=2010-10-31&per_page=15000

# for i in range(1,3093):
#     url = f"https://www.balldontlie.io/api/v1/players/{i}"
#     resp = requests.get(url=url,params=params)
#     jsonResp = resp.json

f = open("2008firstgame.json")
games2008 = json.load(f)

teamRoster2008 = {} 


for game in games2008['data']:
    teamId = game['team']['id']
    if teamId not in teamRoster2008.keys():
        teamRoster2008[teamId] = []
    teamRoster2008[teamId].append(
        {   
            'id': game['player']['id'],
            'first': game['player']['first_name'],
            'last': game['player']['last_name']        
        }
    )

with open('2008roster.json','w') as outfile:
    json.dump(teamRoster2008,outfile,indent=2)
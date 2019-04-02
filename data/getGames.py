import json

data = []
seasons = ["2011","2012","2013", "2014"]


for season in seasons:
    # Get the season data
    f = open(f"data/{season}Games.json")
    games = json.load(f)
    f.close()

    # Open a new file for game data
    outFile = open(f"data/{season}GameResults.csv", "w")
    games = games['data']

    for game in games:
        data = []
        data.append(game['date'][:10])
        data.append(str(game['home_team']['id']))
        data.append(str(game['visitor_team']['id']))

        label = 1 if int(game['home_team_score']) > int(game['visitor_team_score']) else 0

        data.append(str(label))
        outFile.write(','.join(data) + '\n')
    
    outFile.close()

        







        

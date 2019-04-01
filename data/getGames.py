import json

data = []
seasons = ["2008","2009","2010"]


for season in seasons:
    # Get the season data
    f = open(f"{season}Games.json")
    games = json.load(f)
    f.close()

    # Open a new file for game data
    outFile = open(f"{season}GameResults.csv", "w")
    games = games['data']

    for game in games:
        data = []
        data.append(game['date'][:10])
        data.append(str(game['home_team']['id']))
        data.append(str(game['visitor_team']['id']))
        data.append(str(int(int(game['home_team_score']) > int(game['visitor_team_score']))))
        outFile.write(','.join(data) + '\n')
    
    outFile.close()

        







        

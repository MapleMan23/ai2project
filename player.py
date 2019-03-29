import requests
class Player():
    def __init__(self, playerID):
        self.id = playerID
        
    def getSeasonData(self,season):
        url = f"https://www.balldontlie.io/api/v1/stats"
        params = dict(
            player_ids=self.id,
            seasons=season,
            per_page='1500'
        )
        resp = requests.get(url=url,params=params)
        return resp.json()
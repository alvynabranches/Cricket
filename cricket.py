class Team:
    def __init__(self, team_name:str, players:list):
        self.team_name = team_name
        self.players = players


class Batsmen:
    def __init__(self, player_name:str, runs=0, balls=0, fours=0, sixes=0):
        self.player_name = player_name
        self.runs = runs
        self.balls = balls
        self.fours = fours
        self.sixes = sixes

class Bowler:
    def __init__(self, player_name:str, runs=0, balls=0, wickets=0, maidens=0):
        self.player_name = player_name
        self.runs = runs
        self.balls = balls
        self.wickets = wickets
        self.maidens = maidens
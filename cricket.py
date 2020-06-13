class Team:
    def __init__(self, team_name):
        self.team_name = team_name


class Batsmen:
    def __init__(self, player_name):
        self.player_name = player_name

class Bowler:
    def __init__(self, player_name):
        self.player_name = player_name

class Score:
    def __init__(self, match_type:str, batsmen1, batsmen2, runs=0, wickets=0, balls=0):
        self.match_type = match_type
        self.runs = runs
        self.wickets = wickets
        self.balls = balls
        self.batsmen1 = bestmen1
        self.batsmen2 = bestmen2
        self.current_bestmen = [True, False]
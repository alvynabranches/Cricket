class Team:
    def __init__(self, team_name:str, players:list):
        self.team_name = team_name
        self.players = players

    def optional_players(self, optional_players:list):
        self.optional_players = optional_players


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

class WicketKeeper:
    def __init__(self, player_name:str, catches=0, stumpings=0, runouts=0):
        self.player_name = player_name
        self.catches = catches
        self.stumpings = stumpings
        self.runouts = runouts

class Fielder:
    def __init__(self, player_name, catches=0, stumpings=0, runouts=0):
        self.player_name = player_name
        self.catches = catches
        self.stumpings = stumpings
        self.runouts = runouts

class Player:
    def __init__(self, player_name, batting_order=-1, batsmen:bool=True, bowler:bool=True, fielder:bool=True, wicket_keeper:bool=False):
        '''
            player_name => name of the player
        '''
        self.player_name = player_name
        self.batting_order = batting_order
        self.batsmen = Batsmen(player_name)
        if wicket_keeper:
            self.bowler = None
            self.fielder = None
        else:
            self.bowler = Bowler(player_name)
            self.fielder = Fielder(player_name)
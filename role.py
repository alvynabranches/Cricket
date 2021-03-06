class Team:
    def __init__(self, team_name:str, players:list):
        self.team_name = team_name
        self.players = players

    def set_optional_players(self, optional_players:list):
        self.optional_players = optional_players

    def show_batting_scorecard(self):
        pass

    def show_bowling_figures(self):
        pass

    def __str__(self):
        return f"{self.team_name}"

class Batsmen:
    def __init__(self, player_name:str, runs=0, balls=0, fours=0, sixes=0):
        self.player_name = player_name
        self.runs = runs
        self.balls = balls
        self.fours = fours
        self.sixes = sixes

    def get_batting_scorecard(self):
        pass

    def last_10_balls_history(self):
        pass

    def __str__(self):
        return f"{self.player_name}"

class Bowler:
    def __init__(self, player_name:str, runs=0, balls=0, wickets=0, maidens=0):
        self.player_name = player_name
        self.runs = runs
        self.balls = balls
        self.wickets = wickets
        self.maidens = maidens

    def __str__(self):
        return f"{self.player_name}"

class WicketKeeper:
    def __init__(self, player_name:str, catches=0, stumpings=0, runouts=0):
        self.player_name = player_name
        self.catches = catches
        self.stumpings = stumpings
        self.runouts = runouts

    def __str__(self):
        return f"{self.player_name}"

class Fielder:
    def __init__(self, player_name, catches=0, stumpings=0, runouts=0):
        self.player_name = player_name
        self.catches = catches
        self.stumpings = stumpings
        self.runouts = runouts

    def __str__(self):
        return f"{self.player_name}"

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
    
    def get_batting_figures(self):
        pass

    def get_bowling_figures(self):
        pass
    
    def get_fielding_figures(self):
        pass

    def get_wicketkeeping_figures(self):
        pass

    def __str__(self):
        return f"{self.player_name}"
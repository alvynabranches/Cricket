class Score():
    def __init__(self, match_type:tuple, batsmen1:str, batsmen2:str, runs=0, wickets=0, balls=0, extras={'b': 0, 'lb': 0, 'wd': 0, 'nb': 0}, target=None):
        '''
            match_type => takes in 2 parameter in a tuple i.e. (odi or test, no_of_overs or no_of_days)
        '''
        self.match_type = match_type
        self.batsmen1 = batsmen1
        self.batsmen2 = batsmen2
        self.batsmen = [batsmen1, batsmen2]
        self.current_batsmen = [True, False]

        self.runs = runs
        self.wickets = wickets
        self.balls = balls
        self.extras = extras
        self.target = target
    
    def update_score(self, runs, balls=1, wickets=0):
        self.runs += runs
        self.balls += balls
        self.wickets += wickets
        if balls % 6 == 0:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]
        if self.target != None:
            print(f"{self.to_win()[0]} runs from {self.to_win()[1]} balls")
    
    def to_win(self):
        return (self.target - self.runs, self.match_type[1] * 6 - self.balls)

    def zero(self):
        self.update_score(0)

    def one(self):
        self.update_score(1)
        self.current_batsmen[0] != self.current_batsmen[0]
        self.current_batsmen[1] != self.current_batsmen[1]
    
    def two(self):
        self.update_score(2)

    def three(self):
        self.update_score(3)
        self.current_batsmen[0] != self.current_batsmen[0]
        self.current_batsmen[1] != self.current_batsmen[1]

    def four(self):
        self.update_score(4)

    def five(self):
        self.update_score(5)
        self.current_batsmen[0] != self.current_batsmen[0]
        self.current_batsmen[1] != self.current_batsmen[1]

    def six(self):
        self.update_score(6)
    
    def seven(self):
        self.update_score(7)
        self.current_batsmen[0] != self.current_batsmen[0]
        self.current_batsmen[1] != self.current_batsmen[1]

    def noball(self, runs):
        self.update_score(runs+1, 0)
        self.extras['nb'] += (runs+1)
        if runs % 2 == 1:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]

    def catch_out(self, crossed:bool):
        self.update_score(0, 1, 1)
        if crossed:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]
    
    def run_out(self, completed_runs):
        self.update_score(completed_runs, 1, 1)
        if completed_runs % 2 == 0:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]

    def noball_run_out(self, completed_runs):
        self.update_score(completed_runs+1, 0, 1)
        self.extras['nb'] += (completed_runs+1)
        if completed_runs % 2 == 0:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]

    def stumped(self):
        self.update_score(0, 1, 1)
    
    def stumped_wide(self):
        self.extras['wd'] += 1
        self.update_score(1, 0, 1)

    def wide(self, runs):
        self.extras['wd'] += (runs+1)
        self.update_score(runs+1, 0)
        if runs % 2 == 1:
            self.current_batsmen[0] != self.current_batsmen[0]
            self.current_batsmen[1] != self.current_batsmen[1]

    def runout_wide(self, runs):
        self.extras['wd'] += (runs+1)
        self.update_score(runs+1, 0, 1)

    def bold(self):
        self.update_score(runs, 1, 1)

    def hit_wicket(self):
        self.update_score(0, 1, 1)

    def leg_byes(self, runs):
        self.extras['lb'] += runs
        self.update_score(runs)

    def leg_byes_runout(self, runs):
        self.extras['lb'] += runs
        self.update_score(runs, 1, 1)
    
    def byes(self, runs):
        self.extras['b'] += runs
        self.update_score(runs)
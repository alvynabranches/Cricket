class Score_Batting_First:
    def __init__(self, match_type:tuple, batsmen1:str, batsmen2:str, runs=0, wickets=0, balls=0, extras=0):
        '''
            match_type => takes in 2 parameter in a tuple i.e. (odi or test, no_of_overs or no_of_days)
        '''
        self.match_type = match_type
        self.batsmen = [batsmen1, batsmen2]
        self.current_batsmen = [True, False]

        self.runs = runs
        self.wickets = wickets
        self.balls = balls
        self.extras = extras
    
    def update_score(self, runs, balls=1, wickets=0):
        self.runs += runs
        self.balls += balls
        self.wickets += wickets
        if balls % 6 == 0:
            current_batsmen[0] != current_batsmen[0]
            current_batsmen[1] != current_batsmen[1]

    def zero(self):
        self.update_score(0)

    def one(self):
        self.update_score(1)
        current_batsmen[0] != current_batsmen[0]
        current_batsmen[1] != current_batsmen[1]
    
    def two(self):
        self.update_score(2)

    def three(self):
        self.update_score(3)
        current_batsmen[0] != current_batsmen[0]
        current_batsmen[1] != current_batsmen[1]

    def four(self):
        self.update_score(4)

    def five(self):
        self.update_score(5)
        current_batsmen[0] != current_batsmen[0]
        current_batsmen[1] != current_batsmen[1]

    def six(self):
        self.update_score(6)
    
    def seven(self):
        self.update_score(7)
        current_batsmen[0] != current_batsmen[0]
        current_batsmen[1] != current_batsmen[1]

    def noball(self, runs):
        self.update_score(runs+1, 0)
        self.extras += (runs+1)
        if runs % 2 == 1:
            current_batsmen[0] != current_batsmen[0]
            current_batsmen[1] != current_batsmen[1]

    def catch_out(self, crossed:bool):
        self.update_score(0, 1, 1)
        if crossed:
            current_batsmen[0] != current_batsmen[0]
            current_batsmen[1] != current_batsmen[1]
    
    def run_out(self, completed_runs):
        self.update_score(completed_runs, 1, 1)
        if completed_runs % 2 == 0:
            current_batsmen[0] != current_batsmen[0]
            current_batsmen[1] != current_batsmen[1]

    def noball_run_out(self, completed_runs):
        self.update_score(completed_runs, 0, 1)
        self.extras += (completed_runs+1)
        if completed_runs % 2 == 0:
            current_batsmen[0] != current_batsmen[0]
            current_batsmen[1] != current_batsmen[1]

    def stumped(self):
        self.update_score(0, 1, 1)
    
    def stumped_wide(self):
        self.extras += 1
        self.update_score(1, 0, 1)

    def wide(self, runs):
        self.extras += (runs+1)
        self.update_score(runs, 0, 0)

def Score_Batting_Second(Score_Batting_First):
    def __init__(self, match_type:str, batsmen1, batsmen2, target, runs=0, wickets=0, balls=0, extras=0):
        super().__init__(match_type, batsmen1, batsmen2, runs, wickets, balls, extras)
        self.target = target

    def update_score(self, runs, balls=1, wickets=0):
        super.update_score(runs, balls, wickets)

    def zero(self):
        super().zero()

    def one(self):
        super().one()
    
    def two(self):
        super().two()

    def three(self):
        super().three()

    def four(self):
        super().four()

    def five(self):
        super().five()

    def six(self):
        super().six()
    
    def seven(self):
        super().seven()

    def noball(self, runs):
        super().noball(runs)

    def catch_out(self, crossed:bool):
        super().catch_out(crossed)
    
    def run_out(self, completed_runs):
        super().run_out(completed_runs)

    def noball_run_out(self, completed_runs):
        super().noball_run_out(completed_runs)

    def stumped(self):
        super().stumped()

    def stumped_wide(self):
        super().stumped_wide()

    def wide(self):
        super().wide()
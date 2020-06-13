class Score:
    def __init__(self, match_type:str, batsmen1, batsmen2, runs=0, wickets=0, balls=0):
        self.match_type = match_type
        self.runs = runs
        self.wickets = wickets
        self.balls = balls
        self.batsmen = [bestmen1, bestmen2]
        self.current_batsmen = [True, False]
    
    def update_score(self, runs, balls=1, wickets=0):
        self.runs += runs
        self.balls += balls
        self.wickets += wickets

    def zero(self):
        self.update_score(0)

    def one(self):
        self.update_score(1)
    
    def two(self):
        self.update_score(2)

    def three(self):
        self.update_score(3)

    def four(self):
        self.update_score(4)

    def five(self):
        self.update_score(5)

    def six(self):
        self.update_score(6)
    
    def seven(self):
        self.update_score(7)

    def noball(self, runs):
        self.update_score(runs, 0)

    def catch_out(self, crossed:bool):
        self.update_score(0, 1, 1)
    
    def run_out(self, completed_runs):
        self.update_score(completed_runs, 1, 1)

    def noball_run_out(self, completed_runs):
        self.update_score(completed_runs, 0, 1)
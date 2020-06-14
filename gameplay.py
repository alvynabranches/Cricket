from score import Score
from role import Team

class Over:
    def __init__(self, over_no:int):
        self.over_no = over_no
        self.over = []

    def update_over(self, initials):
        self.over.append(str(initials).lower())

    def __str__(self):
        return f"{self.over_no}\t{[d for d in self.over]}"

class Match:
    def __init__(self, match_id, match_no, team_1:Team, team_2:Team):
        self.match_id = match_id
        self.match_no = match_no
        self.team_1 = team_1
        self.team_2 = team_2
        self.team_1_overs = []
        self.team_2_overs = []
        self.field_umpire_1 = str()
        self.field_umpire_2 = str()
        self.third_umpire = str()
        self.referee = str()

    def set_referee(self, referee_name):
        self.referee = referee_name

    def get_referee(self):
        return self.referee

    def set_field_umpires(self, umpire1, umpire2):
        self.field_umpire_1 = umpire1
        self.field_umpire_2 = umpire2

    def get_field_umpires(self):
        return self.field_umpire_1, self.field_umpire_2

    def set_third_umpires(self, umpire_name):
        self.third_umpire = umpire_name

    def get_third_umpires(self):
        return self.third_umpire

    def get_team_1_players(self):
        return self.team_1.players

    def get_team_2_players(self):
        return self.team_2.players

    def __str__(self):
        return f"{self.team_1} vs {self.team_2}"

class Tournament:
    def __init__(self, tournament_id, tournament_name):
        super().__init__()
        self.tournament_id = tournament_id
        self.tournament_name = tournament_name
        self.matches = []

    def set_schedule(self):
        pass

    def get_schedule(self):
        pass

    def __str__(self):
        return f"{self.tournament_name}"

def current_ball(score:Score, over:Over, option):
    '''
        Multiple options are available here for the option attribute
        it can take in options like
        /0 -> dot ball
        /1 -> single run
        /2 -> two runs
        /3 -> three runs
        /4 -> four runs
        /5 -> five runs
        /6 -> six runs
        /7 -> seven runs
        /nb -> no ball
        /nb+* -> no ball + * runs
        /w:coc -> wicket : catch out and crossed over for a single
        /w:co -> wicket : catch out and (crossed over for double or stand still)
        /w:ro -> wicket : run out
        /w:ro+* -> wicket : run out + * runs
        /w:ro+nb -> wicket : run out + no ball
        /w:ro+nb+* -> wicket : run out + no ball + * runs
        /w:s -> wicket : stumped
        /w:s+wd -> wicket : stumped + wide
        /w:b -> wicket : bold
        /w:hw -> wicket : hit wicket
        /*lb -> leg byes
        /w:ro+lb -> wicket : run out + leg byes
        /w:ro+lb+* -> wicket : run out + leg byes + * runs
        /wd -> wide
        /wd+* -> wide + * runs
    '''
    if option == '0':
        score.zero()
        over.update_over(option)
    elif option == '1':
        score.one()
        over.update_over(option)
    elif option == '2':
        score.two()
        over.update_over(option)
    elif option == '3':
        score.three()
        over.update_over(option)
    elif option == '4':
        score.four()
        over.update_over(option)
    elif option == '5':
        score.five()
        over.update_over(option)
    elif option == '6':
        score.six()
        over.update_over(option)
    elif option == '7':
        score.seven()
        over.update_over(option)
    elif option == 'nb':
        score.noball(0)
        over.update_over(option)
    elif option == 'nb+1':
        score.noball(1)
        over.update_over(option)
    elif option == 'nb+2':
        score.noball(2)
        over.update_over(option)
    elif option == 'nb+3':
        score.noball(3)
        over.update_over(option)
    elif option == 'nb+4':
        score.noball(4)
        over.update_over(option)
    elif option == 'nb+5':
        score.noball(5)
        over.update_over(option)
    elif option == 'nb+6':
        score.noball(6)
        over.update_over(option)
    elif option == 'nb+7':
        score.noball(6)
        over.update_over(option)
    elif option == 'w:coc':
        score.catch_out(True)
        over.update_over(option)
    elif option == 'w:co':
        score.catch_out(False)
        over.update_over(option)
    elif option == 'w:ro':
        score.run_out(0)
        over.update_over(option)
    elif option == 'w:ro+1':
        score.run_out(1)
        over.update_over(option)
    elif option == 'w:ro+2':
        score.run_out(2)
        over.update_over(option)
    elif option == 'w:ro+3':
        score.run_out(3)
        over.update_over(option)
    elif option == 'w:ro+4':
        score.run_out(4)
        over.update_over(option)
    elif option == 'w:ro+5':
        score.run_out(5)
        over.update_over(option)
    elif option == 'w:ro+6':
        score.run_out(6)
        over.update_over(option)
    elif option == 'w:ro+7':
        score.run_out(7)
        over.update_over(option)
    elif option == 'w:ro+nb':
        score.noball_run_out(0)
        over.update_over(option)
    elif option == 'w:ro+nb+1':
        score.noball_run_out(1)
        over.update_over(option)
    elif option == 'w:ro+nb+2':
        score.noball_run_out(2)
        over.update_over(option)
    elif option == 'w:ro+nb+3':
        score.noball_run_out(3)
        over.update_over(option)
    elif option == 'w:ro+nb+4':
        score.noball_run_out(4)
        over.update_over(option)
    elif option == 'w:ro+nb+5':
        score.noball_run_out(5)
        over.update_over(option)
    elif option == 'w:ro+nb+6':
        score.noball_run_out(6)
        over.update_over(option)
    elif option == 'w:ro+nb+7':
        score.noball_run_out(7)
        over.update_over(option)
    elif option == 'w:s':
        score.stumped()
        over.update_over(option)
    elif option == 'w:s+wd':
        score.stumped_wide()
        over.update_over(option)
    elif option == 'w:b':
        score.bold()
        over.update_over(option)
    elif option == 'w:hw':
        score.hit_wicket()
        over.update_over(option)
    elif option == '1lb':
        score.leg_byes(1)
        over.update_over(option)
    elif option == '2lb':
        score.leg_byes(2)
        over.update_over(option)
    elif option == '3lb':
        score.leg_byes(3)
        over.update_over(option)
    elif option == '4lb':
        score.leg_byes(4)
        over.update_over(option)
    elif option == '5lb':
        score.leg_byes(5)
        over.update_over(option)
    elif option == '6lb':
        score.leg_byes(6)
        over.update_over(option)
    elif option == '7lb':
        score.leg_byes(7)
        over.update_over(option)
    elif option == 'w:ro+lb':
        score.leg_byes_runout(1)
        over.update_over(option)
    elif option == 'w:ro+lb+2':
        score.leg_byes_runout(2)
        over.update_over(option)
    elif option == 'w:ro+lb+3':
        score.leg_byes_runout(3)
        over.update_over(option)
    elif option == 'w:ro+lb+4':
        score.leg_byes_runout(4)
        over.update_over(option)
    elif option == 'w:ro+lb+5':
        score.leg_byes_runout(5)
        over.update_over(option)
    elif option == 'w:ro+lb+6':
        score.leg_byes_runout(6)
        over.update_over(option)
    elif option == 'w:ro+lb+7':
        score.leg_byes_runout(7)
        over.update_over(option)
    elif option == '1b':
        score.byes(1)
        over.update_over(option)
    elif option == '2b':
        score.byes(2)
        over.update_over(option)
    elif option == '3b':
        score.byes(3)
        over.update_over(option)
    elif option == '4b':
        score.byes(4)
        over.update_over(option)
    elif option == '5b':
        score.byes(5)
        over.update_over(option)
    elif option == '6b':
        score.byes(6)
        over.update_over(option)
    elif option == '7b':
        score.byes(7)
        over.update_over(option)
    elif option == 'wd':
        score.wide(0)
        over.update_over(option)
    elif option == 'wd+1':
        score.wide(1)
        over.update_over(option)
    elif option == 'wd+2':
        score.wide(2)
        over.update_over(option)
    elif option == 'wd+3':
        score.wide(3)
        over.update_over(option)
    elif option == 'wd+4':
        score.wide(4)
        over.update_over(option)
    elif option == 'wd+5':
        score.wide(5)
        over.update_over(option)
    elif option == 'wd+6':
        score.wide(6)
        over.update_over(option)
    elif option == 'wd+7':
        score.wide(7)
        over.update_over(option)
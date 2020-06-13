from score import Score_Batting_First
class Over:
    def __init__(self, over_no:int):
        self.over_no = over_no
        self.over = []

    def update_over(self, initials):
        self.over.append(str(initials).lower())

def current_ball(score:Score_Batting_First, option):
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
        /w:s -> 
        /w:s+wd -> 
        /w:b -> 
        /w:hw -> 
        /*lb -> 
        /w:ro+lb -> 
        /w:ro+lb+* -> 
        wd -> 
        wd+* -> 
    '''
    if option == '0':
        score.zero()
    elif option == '1':
        score.one()
    elif option == '2':
        score.two()
    elif option == '3':
        score.three()
    elif option == '4':
        score.four()
    elif option == '5':
        score.five()
    elif option == '6':
        score.six()
    elif option == '7':
        score.seven()
    elif option == 'nb':
        score.noball(0)
    elif option == 'nb+1':
        score.noball(1)
    elif option == 'nb+2':
        score.noball(2)
    elif option == 'nb+3':
        score.noball(3)
    elif option == 'nb+4':
        score.noball(4)
    elif option == 'nb+5':
        score.noball(5)
    elif option == 'nb+6':
        score.noball(6)
    elif option == 'nb+7':
        score.noball(6)
    elif option == 'w:coc':
        score.catch_out(True)
    elif option == 'w:co':
        score.catch_out(False)
    elif option == 'w:ro':
        score.run_out(0)
    elif option == 'w:ro+1':
        score.run_out(1)
    elif option == 'w:ro+2':
        score.run_out(2)
    elif option == 'w:ro+3':
        score.run_out(3)
    elif option == 'w:ro+4':
        score.run_out(4)
    elif option == 'w:ro+5':
        score.run_out(5)
    elif option == 'w:ro+6':
        score.run_out(6)
    elif option == 'w:ro+7':
        score.run_out(7)
    elif option == 'w:ro+nb':
        score.noball_run_out(0)
    elif option == 'w:ro+nb+1':
        score.noball_run_out(1)
    elif option == 'w:ro+nb+2':
        score.noball_run_out(2)
    elif option == 'w:ro+nb+3':
        score.noball_run_out(3)
    elif option == 'w:ro+nb+4':
        score.noball_run_out(4)
    elif option == 'w:ro+nb+5':
        score.noball_run_out(5)
    elif option == 'w:ro+nb+6':
        score.noball_run_out(6)
    elif option == 'w:ro+nb+7':
        score.noball_run_out(7)
    elif option == 'w:s':
        score.stumped()
    elif option == 'w:s+wd':
        score.stumped_wide()
    elif option == 'w:b':
        score.bold()
    elif option == 'w:hw':
        score.hit_wicket()
    elif option == '1lb':
        score.leg_byes(1)
    elif option == '2lb':
        score.leg_byes(2)
    elif option == '3lb':
        score.leg_byes(3)
    elif option == '4lb':
        score.leg_byes(4)
    elif option == '5lb':
        score.leg_byes(5)
    elif option == '6lb':
        score.leg_byes(6)
    elif option == '7lb':
        score.leg_byes(7)
    elif option == 'w:ro+lb':
        score.leg_byes_runout(1)
    elif option == 'w:ro+lb+2':
        score.leg_byes_runout(2)
    elif option == 'w:ro+lb+3':
        score.leg_byes_runout(3)
    elif option == 'w:ro+lb+4':
        score.leg_byes_runout(4)
    elif option == 'w:ro+lb+5':
        score.leg_byes_runout(5)
    elif option == 'w:ro+lb+6':
        score.leg_byes_runout(6)
    elif option == 'w:ro+lb+7':
        score.leg_byes_runout(7)
    elif option == '1b':
        score.byes(1)
    elif option == '2b':
        score.byes(2)
    elif option == '3b':
        score.byes(3)
    elif option == '4b':
        score.byes(4)
    elif option == '5b':
        score.byes(5)
    elif option == '6b':
        score.byes(6)
    elif option == '7b':
        score.byes(7)
    elif option == 'wd':
        score.wide(0)
    elif option == 'wd+1':
        score.wide(1)
    elif option == 'wd+2':
        score.wide(2)
    elif option == 'wd+3':
        score.wide(3)
    elif option == 'wd+4':
        score.wide(4)
    elif option == 'wd+5':
        score.wide(5)
    elif option == 'wd+6':
        score.wide(6)
    elif option == 'wd+7':
        score.wide(7)
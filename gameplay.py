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
        0
        1
        2
        3
        4
        5
        6
        7
        nb
        nb+*
        w:coc
        w:co
        w:ro
        w:ro+*
        w:ro+nb+*
        w:s
        w:s+wd
        w:b
        w:hw
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
    elif option == 'w+1':
        score.run_out(1)
    elif option == 'w+2':
        score.run_out(2)
    elif option == 'w+3':
        score.run_out(3)
    elif option == 'w+4':
        score.run_out(4)
    elif option == 'w+5':
        score.run_out(5)
    elif option == 'w+6':
        score.run_out(6)
    elif option == 'w+7':
        score.run_out(7)
    elif option == 'nb+w':
        score.noball_run_out(0)
    elif option == 'nb+w+1':
        score.noball_run_out(1)
    elif option == 'nb+w+2':
        score.noball_run_out(2)
    elif option == 'nb+w+3':
        score.noball_run_out(3)
    elif option == 'nb+w+4':
        score.noball_run_out(4)
    elif option == 'nb+w+5':
        score.noball_run_out(5)
    elif option == 'nb+w+6':
        score.noball_run_out(6)
    elif option == 'nb+w+7':
        score.noball_run_out(7)
    elif option == 'w:s':
        score.stumped()
    elif option == 'w:s+wd':
        score.stumped_wide()
    elif option == 'w:b':
        score.bold()
    elif option == 'w:hw':
        score.hit_wicket()
    elif option == 'lb':
        score.leg_byes(1)
    elif option == 'lb+2':
        score.leg_byes(2)
    elif option == 'lb+3':
        score.leg_byes(3)
    elif option == 'lb+4':
        score.leg_byes(4)
    elif option == 'lb+5':
        score.leg_byes(5)
    elif option == 'lb+6':
        score.leg_byes(6)
    elif option == 'lb+7':
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
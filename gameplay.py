class Over:
    def __init__(self, over_no:int):
        self.over_no = over_no
        self.over = []

    def update_over(self, initials):
        self.over.append(str(initials).lower())

def current_ball(score, option):
    if option == '0':
        score.zero()
    elif option == '1':
        score.one()
    elif option == '2':
        score.two()
    elif option == '3':
        pass
    elif option == '4':
        pass
    elif option == '5':
        pass
    elif option == '6':
        pass
    elif option == '7':
        pass
    elif option == '':
        pass
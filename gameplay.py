class Overs:
    def __init__(self, over_no:int):
        self.over_no = over_no
        self.over = []

    def update_over(self, initials):
        self.over.append(str(initials).lower())
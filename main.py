from role import Batsmen, Bowler, WicketKeeper, WicketKeeper, Team, Player
from score import Score
from gameplay import Over, current_ball
from datetime import datetime
from hashlib import sha512

match_id = str(sha512(str(datetime.now()).encode()).hexdigest().encode()).replace("b'", '').replace("'", '')

no_of_players_per_team = int(input('No of Players per Team:\t'))
o = int(input('No of Overs per Team:\t'))
print()

team1 = str(input('Team 1 Name:\t\t'))
team1_players = []
for i in range(no_of_players_per_team):
    team1_players.append(Player(str(input(f"Team 1 Player {i+1}:\t")), batting_order=i+1))

t1 = Team(team1, players=team1_players)
print(t1.team_name)
print(t1.players)
print()

team2 = str(input('Team 2 Name:\t\t'))
team2_players = []
for i in range(no_of_players_per_team):
    team2_players.append(Player(str(input(f"Team 2 Player {i+1}:\t")), batting_order=i+1))

t2 = Team(team2, team2_players)
print(t2.team_name)
print(t2.players)
print()

print("Team 1 playing now")

s1 = Score(('odi', o), t1.players[0], t1.players[1])
t1overs = []
for i in range(o):
    _i = 0
    t1overs.append(Over(i+1))
    while True:
        _i += 1
        _option = str(input()).lower()
        t1overs[i].update_over(_option)
        current_ball(s1, _option)
        print(f"{s1.runs}-{s1.wickets}\t{s1.balls}")
        if s1.balls % 6 == 0 and _i != 1:
            break

print("Team 2 playing now")

s2 = Score(('odi', o), t2.players[0], t2.players[1], target=s1.runs+1)
t2overs = []
for i in range(o):
    _i = 0
    t2overs.append(Over(i+1))
    while True:
        _i += 1
        _option = str(input()).lower()
        t2overs[i].update_over(_option)
        current_ball(s2, _option)
        print(f"{s2.runs}-{s2.wickets}\t{s2.balls}")
        if s2.balls % 6 == 0 and _i != 1:
            break
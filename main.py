from role import Batsmen, Bowler, WicketKeeper, WicketKeeper, Team
from score import Score_Batting_First, Score_Batting_Second
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
    team1_players.append(str(input(f"Team 1 Player {i+1}:\t")))

t1 = Team(team1, players=team1_players)
print(t1.team_name)
print(t1.players)
print()

team2 = str(input('Team 2 Name:\t\t'))
team2_players = []
for i in range(no_of_players_per_team):
    team2_players.append(str(input(f"Team 2 Player {i+1}:\t")))

t2 = Team(team2, team2_players)
print(t2.team_name)
print(t2.players)
print()
s1 = Score_Batting_First(('odi', o), t1.players[0], t1.players[1])
t1overs = []
for i in range(o):
    t1overs.append(Over(i+1))
    while s1.balls % 6 == 0:
        _option = str(input()).lower()
        t1overs[i].update_over(_option)
        
s2 = Score_Batting_Second(('odi', o), t2.players[0], t2.players[1])
t2overs = []
for i in range(o):
    t2overs.append(Over(i+1))
    while s2.balls % 6 == 0:
        _option = str(input()).lower()
        t2overs[i].update_over(_option)
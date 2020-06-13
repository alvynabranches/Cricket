from cricket import Batsmen, Bowler, Team
from score import Score_Batting_First, Score_Batting_Second

no_of_players_per_team = int(input('No of Players per Team:\t'))
overs = int(input('No of Overs per Team:\t'))
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

for i in range(overs):
    while True:
        pass
from cricket import Batsmen, Bowler, Team
from score import Score_Batting_First, Score_Batting_Second

no_of_players_per_team = input('No of Players per Team:\t')
team1 = input('Team 1 Name:\t')
team1_players = []
for i in range(no_of_players_per_team):
    team1_players.append(str(input(f"Team 1 Player {i+1}")))
    
team2 = input('Team 2 Name:\t')
team2_players = []
for i in range(no_of_players_per_team):
    team2_players.append(str(input(f"Team 2 Player {i+1}")))

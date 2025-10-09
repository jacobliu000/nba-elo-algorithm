import json
import pandas as pd

with open("season_start_elos.json", "r") as f:
    ELOS = json.load(f)

K = 20 # variation
H = 34 # home court advantage

df = pd.read_csv("games.csv")
df = df.sort_values(by="gameDate")

for row in df.itertuples(index=True):
    if (row.homeScore > row.awayScore):
        
        S_home = 1
        S_away = 0
    else:
        S_home = 0
        S_away = 1

    R_home = ELOS.get(row.hometeamName.lower(),1500)
    R_away = ELOS.get(row.awayteamName.lower(),1500)

    P_home = (1/(1 + 10 ** ((R_away-(R_home+H))/400)))
    P_away = 1 - P_home



    ELOS[row.hometeamName.lower()] = R_home + K * (S_home - P_home)
    ELOS[row.awayteamName.lower()] = R_away + K * (S_away - P_away)



with open("elos.json", "w") as f:
    json.dump(ELOS, f)
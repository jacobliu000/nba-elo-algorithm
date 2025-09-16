import pandas as pd
import json

start_datetime = "2024-10-21 00:00:00" #for now, start date of 24-25 season
end_datetime = "2025-04-13 00:00:00"

K = 20 # variation
H = 65 # home court advantage

df = pd.read_csv("Games.csv")

df = df.drop(["gameId", "hometeamCity", "hometeamId", "awayteamCity", "awayteamId", "gameType", "attendance", "arenaId", "gameLabel", "gameSubLabel", "seriesGameNumber", "winner"], axis=1)
df["gameDate"] = pd.to_datetime(df["gameDate"])
start_datetime = pd.to_datetime(start_datetime)
end_datetime = pd.to_datetime(end_datetime)
df = df[(df['gameDate'] > start_datetime) & (df['gameDate'] < end_datetime)]
df = df.sort_values(by="gameDate")

ELOS = {}


for row in df.itertuples(index=True):

    if (row.homeScore > row.awayScore):
        S_home = 1
        S_away = 0
    else:
        S_home = 0
        S_away = 1

    R_home = ELOS.get(row.hometeamName,1500)
    R_away = ELOS.get(row.awayteamName,1500)

    P_home = (1/(1 + 10 ** ((R_away-(R_home+H))/400)))
    P_away = 1 - P_home

    ELOS[row.hometeamName] = R_home + K * (S_home - P_home)
    ELOS[row.awayteamName] = R_away + K * (S_away - P_away)

with open("elos.json", "w") as f:
    json.dump(ELOS, f)

#print it out
max_len = max(len(team) for team in ELOS.keys())

for team,rating in sorted(ELOS.items(), key = lambda x : x[1], reverse=True):
    print(f"{team:<{max_len}} : {rating:.2f}")
import pandas as pd
import json

start_datetime = "2024-10-21 00:00:00" #for now, start date of 24-25 season
end_datetime = "2025-04-13 00:00:00"

K = 20 # variation
H = 34 # home court advantage
alpha = 0.9

df = pd.read_csv("past_games.csv")

df = df.drop(["gameId", "hometeamCity", "hometeamId", "awayteamCity", "awayteamId", "gameType", "attendance", "arenaId", "gameLabel", "gameSubLabel", "seriesGameNumber", "winner"], axis=1)
df["gameDate"] = pd.to_datetime(df["gameDate"])
start_datetime = pd.to_datetime(start_datetime)
end_datetime = pd.to_datetime(end_datetime)
df = df[(df['gameDate'] > start_datetime) & (df['gameDate'] < end_datetime)]
df = df.sort_values(by="gameDate")

homepts = {}
awaypts = {}


for row in df.itertuples(index=True):
    h_name = row.hometeamName.lower()
    a_name = row.awayteamName.lower()

    homepts[h_name] = homepts.get(h_name, [])
    awaypts[a_name] = awaypts.get(a_name, [])

    homepts[h_name].append(row.homeScore)
    awaypts[a_name].append(row.awayScore)


for team in homepts.keys():
    homepts[team].sort()

for team in awaypts.keys():
    awaypts[team].sort()

with open("home_points.json", "w") as f:
    json.dump(homepts, f)


with open("away_points.json", "w") as f:
    json.dump(awaypts, f)

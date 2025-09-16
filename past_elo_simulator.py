import pandas as pd

filter_datetime = "2024-10-21 00:00:00" #for now, start date of 24-25 season

K = 20

df = pd.read_csv("Games.csv")

df = df.drop(["gameId", "hometeamCity", "hometeamId", "awayteamCity", "awayteamId", "gameType", "attendance", "arenaId", "gameLabel", "gameSubLabel", "seriesGameNumber", "winner"], axis=1)
df["gameDate"] = pd.to_datetime(df["gameDate"])
filter_datetime = pd.to_datetime(filter_datetime)
df = df[df['gameDate'] > filter_datetime]
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

    P_home = (1/(1 + 10 ** ((R_away-R_home)/400)))
    P_away = 1 - P_home

    ELOS[row.hometeamName] = R_home + K * (S_home - P_home)
    ELOS[row.awayteamName] = R_away + K * (S_away - P_away)

print(ELOS)
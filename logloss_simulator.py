import pandas as pd
from numpy import log as ln

start_datetime = "2024-10-21 00:00:00" #for now, start date of 24-25 season
end_datetime = "2025-04-13 00:00:00"

K = 20 # variation
alpha = 0.9

df = pd.read_csv("past_games.csv")

df = df.drop(["gameId", "hometeamCity", "hometeamId", "awayteamCity", "awayteamId", "gameType", "attendance", "arenaId", "gameLabel", "gameSubLabel", "seriesGameNumber", "winner"], axis=1)
df["gameDate"] = pd.to_datetime(df["gameDate"])
start_datetime = pd.to_datetime(start_datetime)
end_datetime = pd.to_datetime(end_datetime)
df = df[(df['gameDate'] > start_datetime) & (df['gameDate'] < end_datetime)]
df = df.sort_values(by="gameDate")

ELOS = {}


def test_H(h, seed):
    ELOS = {}
    tot = 0
    logloss = 0
    sample = df.sample(frac=0.3, random_state=seed)
    for row in sample.itertuples(index=True):
                

        R_home = ELOS.get(row.hometeamName,1500)
        R_away = ELOS.get(row.awayteamName,1500)

        P_home = (1/(1 + 10 ** ((R_away-(R_home+h))/400)))
        P_away = 1 - P_home
        
        if (row.homeScore > row.awayScore):
            S_home = 1
            S_away = 0
        else:
            S_home = 0
            S_away = 1

        logloss += S_home * ln(P_home) + (1 - S_home) * ln(1 - P_home)

        ELOS[row.hometeamName] = R_home + K * (S_home - P_home)
        ELOS[row.awayteamName] = R_away + K * (S_away - P_away)

        tot += 1


    logloss = -logloss/tot

    print("H=",h, "Loss=", logloss)

#middle = 33
for H in range(50, 71):
    h_real = H/2
    for s in range(67,70):
        test_H(h_real, s)
    print("-")


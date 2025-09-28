import json

def main():

    with open("elos.json", "r") as f:
        ELOS = json.load(f)
    home = input("home:")
    away = input("away:")
    odds = int(input("odds:"))

    implied_odds = 0

    if odds > 0:
        implied_odds = 100/(odds+100)
    else:
        implied_odds = -(odds)/(-odds+100)

    


    if ELOS.get(home,-1)==-1 or ELOS.get(away,-1)==-1:
        print("invalid")
        return 1
    

    print("---")
    print("Implied Odds | home = ", round(100*implied_odds, 3), "% | away = ", round(100*(1-implied_odds), 3), "%")
    H_best = 32
    probability = round(100 * 1/(1+10**((ELOS[away]-ELOS[home]-H_best)/400)),3)
    print("Most Accurate Probability | home =", probability, "% | away = ", 100-probability, "%")
    print("---")

    for H in range(50, 71):
        h_real = H/2
        probability = round(100 * 1/(1+10**((ELOS[away]-ELOS[home]-h_real)/400)),3)
        print("H=",h_real," home win =", probability, "% | away win = ", 100-probability, "%")


main()
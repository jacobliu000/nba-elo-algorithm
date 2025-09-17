import json

def main():

    with open("elos.json", "r") as f:
        ELOS = json.load(f)
    home = input("home:")
    away = input("away:")

    if ELOS.get(home,-1)==-1 or ELOS.get(away,-1)==-1:
        print("invalid")
        return 1
    
    for H in range(45, 86, 4):
        probability = 1/(1+10**((ELOS[away]-ELOS[home]-H)/400))
        print("H=",H," home win probablity=", probability)

main()
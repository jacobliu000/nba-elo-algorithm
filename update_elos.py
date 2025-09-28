import json

with open("season_start_elos.json", "r") as f:
    ELOS = json.load(f)

with open("elos.json", "w") as f:
    json.dump(ELOS, f)
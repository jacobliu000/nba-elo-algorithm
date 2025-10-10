import json

def team_overunder(is_home, OU, team):
    if is_home:
        with open("home_points.json", "r") as f:
            points = json.load(f)
    else:
        with open("away_points.json", "r") as f:
            points = json.load(f)
        
    pts = points[team]
    left = 0
    right = len(pts)
    

    while left < right:
        mid = (right + left) // 2

        if pts[mid] > OU:
            right = mid - 1
        else:
            left = mid + 1


    under = left 
    over = len(pts)-under
    
    print("under: ", round(under/len(pts)*100,2), "%")
    print("over: ", round(over/len(pts)*100,2), "%")



team_overunder(False, 118.5, "cavaliers")
team_overunder(True, 114.5, "bulls")


def GetManhattanDist(directions):
    rd = {"N": "E", "E": "S", "S":"W", "W": "N" }
    ld = {"N":"W", "W": "S", "S": "E", "E":"N"}
    sd = "E"
    x = 0
    y = 0

    for d in directions:
        if d[0] == "N":
            y += d[1]
        elif d[0] == "S":
            y -= d[1]
        elif d[0] == "E":
            x += d[1]
        elif d[0] == "W":
            x -= d[1]
        elif d[0] == "R":
            for i in range(int(d[1]/90)):
                sd = rd[sd]
        elif d[0] == "L":
            for i in range(int(d[1]/90)):
                sd = ld[sd]
        elif d[0] == "F":
            if sd == "E":
                x += d[1]
            if sd == "W":
                x -= d[1]
            if sd == "N":
                y += d[1]
            if sd == "S":
                y -= d[1]
        print(f"{d}, {x}, {y}")
    return abs(x) + abs(y)

def WaypointDist(directions):

    rd = {"N": "E", "E": "S", "S":"W", "W": "N" }
    ld = {"N":"W", "W": "S", "S": "E", "E":"N"}
    sd = "N"
    x = 0
    y = 0

    waypoint = [10, 1]

    for d in directions:
        if d[0] == "N":
            waypoint[1] += d[1]
        elif d[0] == "S":
            waypoint[1] -= d[1]
        elif d[0] == "E":
            waypoint[0] += d[1]
        elif d[0] == "W":
            waypoint[0] -= d[1]
        elif d[0] == "R":
            for i in range(int(d[1]/90)):
                Rotate(waypoint, sd, True)
                sd = rd[sd]
        elif d[0] == "L":
            for i in range(int(d[1]/90)):
                Rotate(waypoint, sd, False)
                sd = ld[sd]
        elif d[0] == "F":
            x += waypoint[0] * d[1]
            y += waypoint[1] * d[1]
        #print(f"Waypoint: {waypoint}")
        #print(f"Ship: {x}, {y}")
        #input()
    return abs(x) + abs(y)


def Rotate(waypoint, old, right):
    waypoint[0], waypoint[1] = waypoint[1], waypoint[0]
    if right: 
        waypoint[1] *= -1
    else:
        waypoint[0] *= -1
    '''
    if old == "N":
        if right: 
            waypoint[1] *= -1
        else:
            waypoint[0] *= -1
    if old == "E":
        if right: 
            waypoint[1] *= -1
        else:
            waypoint[0] *= -1
    if old == "E":
        if right: 
            waypoint[1] *= -1
        else:
            waypoint[0] *= -1
    if old == "E":
        if right: 
            waypoint[1] *= -1
        else:
            waypoint[0] *= -1
    '''

if __name__ == "__main__":

    inputFile = open("Day12Input.txt")

    directions = inputFile.readlines()

    directions = [(l[0], int(l[1:])) for l in (l.strip() for l in directions)]

    #print(directions)

    print(WaypointDist(directions))

    inputFile.close()
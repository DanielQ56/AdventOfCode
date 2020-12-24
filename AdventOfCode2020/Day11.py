
def GetFilledSeats(seats):

    changes = -1
    while changes != 0:
        #PrintList(seats)
        #input()
        changes = ShiftSeats(seats)
    
    print("\nFINAL:\n")
    PrintList(seats)
    #input()

    filled = 0
    for i in range(len(seats)):
        for j in range(len(seats[0])):
            if seats[i][j] == "#":
                filled += 1
    
    return filled

def ShiftSeats(seats):
    sc = [seat.copy() for seat in seats]

    rows = len(sc)
    cols = len(sc[0])

    changes = 0
    for i in range(rows):
        for j in range(cols):
            if sc[i][j] == 'L':
                t = CheckAllDirections(sc, i, j)
                if t == 0:
                    seats[i][j] = "#"
                    changes += 1
            elif sc[i][j] == "#":
                t = CheckAllDirections(sc, i, j)
                #print(f"{i}, {j}, {t}")
                #input()
                if t >= 5:
                    seats[i][j] = "L"
                    changes += 1
    
    return changes
        
def PrintList(seats):
    for row in seats:
        print(row)
    print("\n")

def CheckAdjacent(seats, row, col):
    t = 0

    for i in range(row-1, row+2, 1):
        for j in range(col-1, col+2, 1):
            if i >= 0 and i < len(seats) and j >= 0 and j < len(seats[i]) and not (i == row and j == col):
                if seats[i][j] == "#":
                    t += 1

    return t

def CheckAllDirections(seats, row, col):

    t = 0

    if CheckDirection(seats, row, col, -1, 0) == "#":
        t += 1
    if CheckDirection(seats, row, col, -1, 1) == "#":
        t += 1
    if CheckDirection(seats, row, col, 0, 1) == "#":
        t += 1
    if CheckDirection(seats, row, col, 1, 1) == "#":
        t += 1
    if CheckDirection(seats, row, col, 1, 0) == "#":
        t += 1
    if CheckDirection(seats, row, col, 1, -1) == "#":
        t += 1
    if CheckDirection(seats, row, col, 0, -1) == "#":
        t += 1
    if CheckDirection(seats, row, col, -1, -1) == "#":
        t += 1

    return t


def CheckDirection(seats, row, col, rd, cd):

    i = row + rd
    j = col + cd
    
    while i >= 0 and i < len(seats) and j >= 0 and j < len(seats[i]):
        if seats[i][j] == ".":
            i += rd
            j += cd
        else:
            return seats[i][j]
    return "."


if __name__ == "__main__":
    inputFile = open("Day11Input.txt")

    seats = inputFile.readlines()
    seats = [seat.strip() for seat in seats]

    for i in range(len(seats)):
        seats[i] = [s for s in seats[i]]

    print(GetFilledSeats(seats))

    inputFile.close()
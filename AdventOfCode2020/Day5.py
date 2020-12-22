from math import floor
from math import ceil

def GetHighestSeatID(seats):
    highestSeatID = -1

    for seat in seats:
        seatID = GetID(seat)
        highestSeatID = seatID if seatID >= highestSeatID else highestSeatID

    return highestSeatID

def GetID(seat):
    lowR = 0
    highR = 127
    lowC = 0
    highC = 7
    
    if(len(seat) != 10):
        return -1

    #print(f"Seat: {seat}")

    for i in range(len(seat)):
        if i < 7:
            if seat[i] == "F":
                highR = floor((lowR + highR)/2)
            elif seat[i] == "B":
                lowR = ceil((lowR + highR)/2)
            
            #print(f"{seat[i]}, {lowR}, {highR}")
        else:
            if seat[i] == "L":
                highC = floor((lowC + highC)/2)
            elif seat[i] == "R":
                lowC = ceil((lowC + highC)/2)
            #print(f"{seat[i]}, {lowC}, {highC}")
        #input()

    return lowR * 8 + lowC

def GetUserSeat(seats):
    s = []

    for seat in seats:
        s.append(GetID(seat))

    s.sort()

    for i in range(0, len(s)-1):
        if(s[i + 1]  - s[i] == 2):
            return s[i] + 1

    return -1


if __name__ == "__main__":

    inputFile = open("Day5Input.txt")

    seats = inputFile.readlines()

    seats = [seat.strip() for seat in seats]

    #print(GetID("FBFBBFFRLR"))
    #print(GetHighestSeatID(seats))
    print(GetUserSeat(seats))
    inputFile.close()


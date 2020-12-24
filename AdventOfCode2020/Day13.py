
def FindWaitTime(earliest, shuttles):

    index = 0
    waitTime = float('inf')
    for i, s in enumerate(shuttles):
        nextTime = earliest - (earliest % s) + s
        if nextTime - earliest < waitTime:
            waitTime = nextTime - earliest
            index = i
    return waitTime * shuttles[index]


def FindPattern(shuttles):

    shuttles = [int(s) if s != "x" else "x" for s in shuttles ]

    offset = [i for i in range(len(shuttles)) if shuttles[i] != "x"]
    shuttles = [s for s in shuttles if s != "x"]

    first = shuttles[0]

    m = max(shuttles)
    shift = m + offset[shuttles.index(m)]
    print(shift)
    input()
    while not CheckForCorrectOffset(offset, shuttles, first):
        first += shuttles[0]
        #print(first)
    return first 

def CheckForCorrectOffset(offset, shuttles, first):
    for i in range(len(shuttles)):
        if (first + offset[i]) %shuttles[i] != 0:
            return False
    return True


if __name__ == "__main__":

    inputFile = open("Day13Input.txt")

    i = [line.strip() for line in inputFile.readlines()]

    allshuttles = i[1].split(",")

    earliest = int(i[0])
    shuttles = [int(s) for s in i[1].split(",") if s != "x"]


    
    print(FindPattern(allshuttles))

    inputFile.close()

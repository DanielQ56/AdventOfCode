
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
    a = [shuttles[i] - i for i in range(len(shuttles)) if shuttles[i] != "x"]
    m = [shuttles[i] for i in range(len(shuttles)) if shuttles[i] != "x"]

    a[0] = 0

    M = 1
    for n in m:
        M *= n
    z = [int(M/m[i]) for i in range(len(m))]

    y = [FindY(z[i], m[i]) for i in range(len(m))]

    print(a)
    print(z)
    print(y)
    print(m)


    x = 0
    for i in range(len(m)):
        x += (a[i] * y[i] * z[i])
    
    return x%M

def FindY(z, m):
    y = 0
    while (z*y) % m != 1:
        y += 1
    
    return y

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

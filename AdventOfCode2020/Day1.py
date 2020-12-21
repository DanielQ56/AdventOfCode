
def FindMatch(num, numList):

    firstIndex = 0
    lastIndex = len(numList) - 1

    while firstIndex < lastIndex:
        s = numList[firstIndex] + numList[lastIndex]
        if s < num:
            firstIndex += 1
        elif s > num:
            lastIndex -= 1
        else:
            return numList[firstIndex] * numList[lastIndex]

    return -1

def FindTripleMatch(num, numList):
    for n in numList:
        mult = FindMatch(num - n, numList)
        if mult != -1:
            return mult * n

    return -1

if __name__ == "__main__":

    inputFile = open("Day1Input.txt")
    lines = inputFile.readlines()

    entries = [int(i.strip()) for i in lines]

    entries.sort()

    print(FindTripleMatch(2020, entries))

    inputFile.close()
    
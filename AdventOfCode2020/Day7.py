import re

def CreateBagDictionaryNoNum(allbags):
    bags = {}

    for bag in allbags:
        bag = bag.replace("bags", "bag").split("contain")
        mainBag = bag[0].strip()
        secondaryBags = [i.strip(' .\n') for i in re.sub('\d', '', bag[1]).split(",")]
        #print(f"Bag: {mainBag}, {secondaryBags}")
        if mainBag in bags:
            bags[mainBag].extend(secondaryBags)
        else:
            bags[mainBag] = secondaryBags
        #input()

    print("Done creating bags")

    return bags

def CreateBagDictionaryNum(allbags):
    bags = {}

    for bag in allbags:
        bag = bag.replace("bags", "bag").split("contain")
        mainBag = bag[0].strip()
        secondaryBags = [i.strip(' .\n') for i in bag[1].split(",")]
        #print(f"Bag: {mainBag}, {secondaryBags}")
        if mainBag in bags:
            bags[mainBag].extend(secondaryBags)
        else:
            bags[mainBag] = secondaryBags
        #input()

    print("Done creating bags")

    return bags

def GetStartingBags(allbags):
    bags = CreateBagDictionaryNoNum(allbags)

    count = 0

    for bag in bags.keys():
        #print(f"Bag: {bag}")
        if CheckIfStartingBag(bag, bags):
            #print("starting bag")
            count += 1

        #input()

    return count

def GetNumBags(allbags):
    bags = CreateBagDictionaryNum(allbags)


    return GetNumBagsInBag(1, "shiny gold bag", bags) - 1



def GetNumBagsInBag(num, bag, allbags):
    if bag == "no other bag":
        #print(f"Hit the end: {num}")
        return 0
    else:
        sb = allbags[bag]
        s = 0

        #print(num, bag, sb)
        #input()
        for b in sb:
            if b == "no other bag":
                s += GetNumBagsInBag(num, b, allbags)
            else:
                s += GetNumBagsInBag(num * int(b[0]), b[2:], allbags)
        #print(f"S: {s}")
        #input()
        return s + num


def CheckIfStartingBag(bag, bags):
    q = []

    q.append(bag)

    while len(q) > 0:
        b = q.pop(0)
        for other in bags[b]:
            if other == "shiny gold bag":
                return True
            else:
                if not other in q and other != "no other bag":
                    q.append(other)
    return False

if __name__ == "__main__":

    inputFile = open("Day7Input.txt")

    allbags = inputFile.readlines()

    print(GetNumBags(allbags))

    inputFile.close()
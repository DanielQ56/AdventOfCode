
def FindDistribution(adapters):
    dist = {
        "1": 0,
        "2": 0,
        "3": 1
    }

    adapters.sort()

    dist[str(adapters[0])] += 1

    for i in range(len(adapters) - 1):
        dist[str(adapters[i + 1] - adapters[i])] += 1

    return dist["3"] * dist["1"]


def GetArrangements(adapters):
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)

    d = {}

    for num in adapters:
        d[num] = 0

    d[0] = 1

    for i in range(len(adapters)):

        index = i + 1
        while index < len(adapters) and (adapters[index] - adapters[i]) < 4:
            d[adapters[index]] += d[adapters[i]]
            index += 1
    
    return d[adapters[len(adapters)-1]]


        
def GetNum(adapters):
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[len(adapters) - 1] + 3)
    print(adapters)
    return RecursiveGetArrangements(0, adapters)

def RecursiveGetArrangements(index, adapters):
    if index >= len(adapters) - 1:
        #print("Hit the bottom")
        return 1
    else: 
        s = 0
        i = index + 1
        while i < len(adapters) and (adapters[i] - adapters[index] < 4):
            r = RecursiveGetArrangements(i, adapters)
            #print(f"Current Num: {adapters[index]}, Child: {adapters[i]}, Num Children: {r}")
            #input()
            s += r
            i += 1
        #print(f"Total: {s}")
        return s

if __name__ == "__main__":

    inputFiles = open("Day10Input.txt")

    adapters = inputFiles.readlines()

    adapters = [int(a) for a in adapters]

    print(GetArrangements(adapters))

    inputFiles.close()



'''
        count = 0
        index = i + 1
        while index < len(adapters) and (adapters[index] - adapters[i]) < 4:
            count += 1
            index += 1
            d[]
            print(f"Current: {adapters[i]}, Checking: {adapters[index - 1]}, Count: {count}")
        if count > 1:
            children = [1 for j in range(len(children) * count)]
        print(children)
        input()
    
'''

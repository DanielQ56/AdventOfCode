
def GetNumTrees(path):
    trees = 0

    length = len(path[0])

    pos = 0

    for line in path:
        if line[pos%length] == "#":
            trees += 1
        pos += 3
    
    return trees
    
def GetNumTrees(xslope, yslope, path):
    trees = 0

    length = len(path[0])

    pos = 0

    for i in range(0, len(path), yslope):
        line = path[i]

        if line[pos % length] == "#":
            trees += 1
        pos += xslope

    
    return trees
    

if __name__ == "__main__":

    inputFile = open("Day3Input.txt")

    lines = inputFile.readlines()

    paths = [i.strip() for i in lines]

    print(GetNumTrees(1, 1, paths) * GetNumTrees(3, 1, paths) * GetNumTrees(5, 1, paths) * GetNumTrees(7, 1, paths) * GetNumTrees(1, 2, paths))

    inputFile.close()


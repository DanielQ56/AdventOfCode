
def GetAccumulator(lines):
    acc = 0

    pl = [[line[0], (1 if line[1][0] == "+" else -1) * int(line[1][1:]), 0] for line in (line.split(' ') for line in lines)]

    index = 0
    while index < len(pl) and index >= 0:
        command = pl[index]

        if command[2] == 1:
            break

        pl[index][2] = 1

        if command[0] == "nop": 
            index += 1
        elif command[0] == "acc":
            acc += command[1]
            index += 1
        elif command[0] == "jmp":
            index += command[1]
    
    return acc

    
def FixLines(lines):
    
    pl = [[line[0], (1 if line[1][0] == "+" else -1) * int(line[1][1:]), 0] for line in (line.split(' ') for line in lines)]

    index = len(pl) - 2
    while index < len(pl) and index >= 0:
        if command[0] == "nop": 
            index += 1
        elif command[0] == "acc":
            acc += command[1]
            index += 1
        elif command[0] == "jmp":
            index += command[1]




if __name__ == "__main__":
    inputFile = open ("Day8Input.txt")

    lines = inputFile.readlines()

    print(GetAccumulator(lines))


    inputFile.close()
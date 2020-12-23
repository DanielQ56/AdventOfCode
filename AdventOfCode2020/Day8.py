
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

    
def GetFixedAccumulator(lines):
    acc = 0
    index = 0
    pl = FixLines(lines)

    while index < len(pl) and index >= 0:
        command = pl[index]

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
    loop = []
    index = 0

    startloop = -1
    while index < len(pl) and index >= 0:
        command = pl[index]

        if command[2] == 1:
            loop.append(index)
        elif command[2] == 2:
            break

        pl[index][2] += 1
        if command[0] == "nop": 
            index += 1
        elif command[0] == "acc":
            index += 1
        elif command[0] == "jmp":
            index += command[1]
    for i in loop:
        if pl[i][0] == "nop":
            pl[i][0] = "jmp"
            if CheckIfLoop(pl):
                return pl
            pl[i][0] = "nop"
        elif pl[i][0] == "jmp":
            pl[i][0] = "nop"
            if CheckIfLoop(pl):
                return pl
            pl[i][0] = "jmp"

    return pl

    


def CheckIfLoop(loop):
    
    for l in loop:
        l[2] = 1

    index = 0

    while index >= 0 and index < len(loop):
        command = loop[index] 
        if command[2] == 2:
            return False

        loop[index][2] = 2

        if command[0] == "nop": 
            index += 1
        elif command[0] == "acc":
            index += 1
        elif command[0] == "jmp":
            index += command[1]
    
    if index != len(loop):
        return False

    return True



if __name__ == "__main__":
    inputFile = open ("Day8Input.txt")

    lines = inputFile.readlines()

    print(GetFixedAccumulator(lines))


    inputFile.close()
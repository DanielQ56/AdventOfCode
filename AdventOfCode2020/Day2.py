
def CountValid(entries):
    valid = 0
    for ent in entries:
        numLetter = 0
        for letter in ent[3]:
            if letter == ent[2]:
                numLetter += 1
        if ent[0] <= numLetter and numLetter <= ent[1]:
            valid += 1
    return valid

def CountValid2(entries):
    valid = 0
    for ent in entries:
        # print((ent[3], ent[3][ent[0] - 1], ent[3][ent[1]-1],  ent[2]))
        # print(( ent[3][ent[0] - 1] == ent[2] and ent[3][ent[1]-1] != ent[2]) or ( ent[3][ent[0] - 1] != ent[2] and ent[3][ent[1]-1] == ent[2]))
        # input()
        if ( ent[3][ent[0] - 1] == ent[2] and ent[3][ent[1]-1] != ent[2]) or ( ent[3][ent[0] - 1] != ent[2] and ent[3][ent[1]-1] == ent[2]):
            valid +=1 
    return valid

if __name__ == "__main__":
    inputFile = open("Day2Input.txt")

    inputLines = inputFile.readlines()

    lines = [entry.strip().split(" ") for entry in inputLines]
    passwords = [(int(ent[0].split("-")[0]), int(ent[0].split("-")[1]), ent[1][:1], ent[2]) for ent in lines]
    print(CountValid2(passwords))

    inputFile.close()
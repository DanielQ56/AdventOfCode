import re


def GetValidPassports(passports):
    valid = 0
    passDict = {
        "byr": 0, 
        "iyr": 0,
        "eyr": 0,
        "hgt": 0, 
        "hcl": 0, 
        "ecl": 0, 
        "pid": 0, 
        "cid": 0
    }

    for passport in passports:
        port = passport.replace(" ", "\n")
        pp = port.split("\n")
        for field in pp:
            values = field.split(":")
            passDict[values[0]] = 1
        
        values = [val for val in passDict.values() if val == 1]
        if(len(values) == len(passDict.keys())) or (len(values)== len(passDict.keys()) - 1 and passDict["cid"] == 0):
            valid += 1

        for key in passDict.keys():
            passDict[key] = 0


    return valid

def GetSpecificValidPassport(passports):
    valid = 0
    passDict = {
        "byr": 0, 
        "iyr": 0,
        "eyr": 0,
        "hgt": 0, 
        "hcl": 0, 
        "ecl": 0, 
        "pid": 0, 
        "cid": 0
    }

    for passport in passports:
        port = passport.replace(" ", "\n")
        pp = port.split("\n")
        #print(pp)
        for field in pp:
            values = field.split(":")
            if values[0] in passDict:
                val = 1 if CheckValidField(values[0], values[1]) else 0
                #print(f"Value: {val}")
                #input()
                passDict[values[0]] = val
        
        values = [val for val in passDict.values() if val == 1]
        #print(f"Length Val: {len(values)}")
        #input()
        if(len(values) == len(passDict.keys())) or (len(values)== len(passDict.keys()) - 1 and passDict["cid"] == 0):
            #print("VALID")
            valid += 1

        for key in passDict.keys():
            passDict[key] = 0

    return valid

def CheckValidField(field, value):
    #print(f"{field}, {value}")
    if field == "byr":
        if int(value) >= 1920 and int(value) <= 2002:
            return True
    elif field == "iyr":
        if int(value) >= 2010 and int(value) <= 2020:
            return True
    elif field == "eyr":
        if int(value) >= 2020 and int(value) <= 2030:
            return True
    elif field == "hgt":
        if "in" in value and not("cm" in value):
            val = value[:-2]
            #print(f"Value: {value}, Match: {int(val) >= 59 and int(val) <= 76}")
            #input()
            return int(val) >= 59 and int(val) <= 76
        if "cm" in value and not ("in" in value):
            val = value[:-2]
            #print(f"Value: {value}, Match: {int(val) >= 150 and int(val) <= 193}")
            #input()
            return int(val) >= 150 and int(val) <= 193
    elif field == "hcl":
        return re.search(r'^#[0-9a-f]{6}$', value) != None
    elif field == "ecl":
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif field == "pid":
        return re.search(r"^[0-9]{9}$", value) != None
    elif field == "cid":
        return True

    return False




if __name__ == "__main__":

    inputFile = open("Day4Input.txt")

    content = inputFile.read()

    passports = content.split("\n\n")
    

    print(GetSpecificValidPassport(passports))

    inputFile.close()
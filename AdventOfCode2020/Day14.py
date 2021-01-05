import re
import math

def Mem(lines):
    mem = {}

    mask = ""
    
    for line in lines:
        if "mask" in line:
            mask = line.split("=")[1].strip()
        else:
            vals = list(map(int, re.findall(r'\d+', line)))
            address = vals[0]
            value = vals[1]
            mem[address] = ConvertToValue(GetValue(mask, value))
        
    sum = 0
    for v in mem.values():
        sum += v

    return sum

def Address(lines):
    mem = {}

    mask = ""
    
    for line in lines:
        if "mask" in line:
            mask = line.split("=")[1].strip()
        else:
            vals = list(map(int, re.findall(r'\d+', line)))
            address = vals[0]
            value = vals[1]
            GetAddress(mem, value, mask, address)
        
    sum = 0
    for v in mem.values():
        sum += v

    return sum


def GetAddress(mem, value, mask, address):
    allAddresses = [0]
    add = ConvertToBits(address)

    index = 0
    while index < len(mask):
        if mask[len(mask) - 1 - index] == "0": 
            for i in range(len(allAddresses)): 
                allAddresses[i] += math.pow(2, index) * int(add[len(add) - 1 - index]) if index < len(add) else 0
        elif mask[len(mask) - 1 - index] == "1":
            for i in range(len(allAddresses)):
                allAddresses[i] += math.pow(2, index)
        else:
            orig = len(allAddresses)
            for i in range(orig):
                allAddresses.append(allAddresses[i] + math.pow(2, index))
        index += 1

    for a in allAddresses:
        mem[a] = value
    



def GetValue(mask, value):
    v = ""
    index = 0
    val = ConvertToBits(value)
    while index < len(mask): 
        v = (mask[len(mask) - 1 - index] if mask[len(mask) - 1 - index] != "X" else (val[len(val) - 1 - index] if index < len(val) else "0")) + v
        index += 1

    return v

def ConvertToBits(value):
    b = ""
    while value != 0:
        b = ("1" if value % 2 == 1 else "0") + b
        value = math.floor(value / 2)
    return b

def ConvertToValue(bits):
    v = 0
    for i in range(len(bits)-1, -1, -1):
        v += math.pow(2, int(bits[i]) * (len(bits) - 1 - i)) if int(bits[i]) == 1 else 0
    return int(v)

if __name__ == "__main__":
    inputFile = open("Day14Input.txt")

    lines = inputFile.readlines()

    print(Address(lines))

    inputFile.close()
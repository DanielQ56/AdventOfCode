import re
import math

class Node:
    def __init__(self, r = None, l = None, mid = None):
        self.r = r
        self.l = l
        self.mid = mid
        self.left = None
        self.right = None

class Section:
    def __init__(self, s, r):
        self.range = r
        self.sec = s


possFields = {}

def FindFields(inp):
    sec = inp[0].split("\n")
    yt = inp[1].split("\n")[1].split(",")
    nt = inp[2].split("\n")[1:]
    sections = {}
    possFields = {}
    secNames = []
    for i, s in enumerate(sec): 
        v = list(map(int, re.findall(r'\d+', s)))
        sn = s.split(":")[0]
        secNames.append(sn)
        sections[sn] = [(v[i], v[i + 1]) for i in range(0, len(v) - 1, 2)]

    for i in range(len(yt)):
        possFields[i] = secNames.copy()

    print(len(nt))
    ntc = nt.copy()
    invalid = False
    inv = 0

    for t in nt:
        vals = t.split(",")
        for i,val in enumerate(vals):
            inv = 0
            for k in sections.keys():
                r1 = sections[k][0]
                r2 = sections[k][1]
                if not(r1[0] <= int(val) and int(val) <= r1[1]) and not(r2[0] <= int(val) and int(val) <= r2[1]):
                    inv += 1
            if inv == len(secNames):
                ntc.remove(t)
                break

    print(len(ntc))

    for t in ntc: 
        vals = t.split(',')
        for i, val in enumerate(vals):
            for k in sections.keys():
                r1 = sections[k][0]
                r2 = sections[k][1]
                if not(r1[0] <= int(val) and int(val) <= r1[1]) and not(r2[0] <= int(val) and int(val) <= r2[1]):
                    if k in possFields[i]:
                        possFields[i].remove(k)
                

    allValues = sorted([v for v in possFields.values() ], key = lambda x: len(x))


    for i, v in enumerate(allValues):
        if len(v) == 1: 
            item = v[0]
            for k in possFields.keys():
                if item in possFields[k] and len(possFields[k]) > 1:
                    possFields[k].remove(item)
            for j in range(i + 1, len(allValues)):
                if item in allValues[j]:
                    allValues[j].remove(item)

    print(possFields)

    m = 1
    for i in range(len(yt)):
        if 'departure' in possFields[i][0]:
            print(yt[i])
            m *= int(yt[i])

    return m




def ErrorRate(inp):
    sec = inp[0].split("\n")
    yt = inp[1].split("\n")[1].split(",")
    nt = inp[2].split("\n")[1:]

    sections = []
    secNames = []
    for s in sec:
        v = list(map(int, re.findall(r'\d+', s)))
        sn = s.split(":")[0]
        secNames.append(sn)
        sections.extend([Section(sn, (v[i], v[i + 1])) for i in range(0, len(v) - 1, 2)])


    for i in range(len(yt)):
        possFields[i] = set(secNames)
    

    sections = sorted(sections, key = lambda x: x.range[0])

    root = CreatePST(sections)
    ntc = nt.copy()

    invalid = 0

    for t in nt: 
        vals = t.split(",")
        for v in vals:
            if not SearchPST(root, int(v)):
                invalid += int(v)
    return invalid

    #             ntc.remove(t)

    # for t in ntc: 
    #     vals = t.split(",")
    #     for i in range(len(vals)):
    #         s = set()
    #         GetPossibleFields(root, i, int(vals[i]), s)
    #         possFields[i] = possFields[i].intersection(s)
    
    # allValues = sorted([v for v in possFields.values()], key = lambda x: len(x))
    # print(allValues)

    # for i in range(len(v))

    # print(possFields)


def GetPossibleFields(n, index, val, fields):
    if n is None:
        return False
    else:
        for r in n.l:
            # print(f"{r}, {val}")
            # input()
            if r.range[0] <= val and val <= r.range[1]:
                fields.add(r.sec)
        GetPossibleFields(n.left,index, val, fields)
        for r in n.r:
            # print(f"{r}, {val}")
            # input()
            if r.range[0] <= val and val <= r.range[1]:
                fields.add(r.sec)
        return GetPossibleFields(n.right,index, val, fields)


def SearchPST(n, val):
    if n is None:
        return False
    else:
        if val < n.mid:
            for r in n.l:
                # print(f"{r}, {val}")
                # input()
                if r.range[0] <= val and val <= r.range[1]:
                    return True
            return SearchPST(n.left, val)
        else:
            for r in n.r:
                # print(f"{r}, {val}")
                # input()
                if r.range[0] <= val and val <= r.range[1]:
                    return True
            return SearchPST(n.right, val)

def CreatePST(sections):
    if len(sections) == 0:
        return None
    else:

        mid = int(math.floor(len(sections)/2))

        endpoints = []

        for s in sections:
            endpoints.append(s.range[0])
            endpoints.append(s.range[1])

        endpoints.sort()

        mid = int(math.floor(len(endpoints)/2))

        median = (endpoints[mid] + endpoints[mid - 1]) / 2

        overlap = [s for s in sections if s.range[0] <= median and median <= s.range[1]] 

        n = Node()
        n.l = overlap
        n.r = sorted(overlap.copy(), key = lambda x: x.range[1])
        n.mid = median

        n.left = CreatePST([s for s in sections if s.range[1] < n.mid])
        n.right = CreatePST([s for s in sections if s.range[0] > n.mid])
        return n

def PrintPST(n):
    if not n is None:
        print(n.l)
        PrintPST(n.left)
        PrintPST(n.right)



if __name__ == "__main__":
    inputFile = open("Day16Input.txt")

    sections = inputFile.read().split("\n\n")

    print(FindFields(sections))

    inputFile.close()
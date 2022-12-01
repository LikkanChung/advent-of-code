import re

bagDict = {}

def reverseLookup(bag):
    containedBy = {None}
    for x in bagDict:
        if bag in bagDict[x]:
            containedBy.add(x)
    return containedBy

with open('in.txt') as f:
    lines = f.read().split('\n')

    count = 0
    

    ## input into data structure
    for line in lines:
        match = re.search(r"(\w+\s\w+)\sbags?\scontain\s([a-z0-9\s,]*)", line)

        fromBag = ""
        toBags = []
        if (match != None and len(match.groups()) != 0):
            #print("### " + line)
            
            fromBag = match.group(1) 
            toBagsStr = match.group(2).split(", ")
            for bag in toBagsStr:
                mbag = re.search(r"\d+\s(\w+\s\w+)\sbags?", bag)
                if mbag != None and len(mbag.groups()) != 0:
                    toBags.append(mbag.group(1))
                elif "no other bags" in bag: 
                    toBags.append(None)
            #print(fromBag + " -> " + str(toBags))
            bagDict.update({fromBag: toBags})
    #print(bagDict)

    target = "shiny gold"

    canContainTarget = {None}

    searchSet = {target}

    while len(searchSet) != 0:
        searchItem = searchSet.pop()
        if searchItem != None:
            if searchItem != target:
                canContainTarget.add(searchItem)
            for x in reverseLookup(searchItem):
                searchSet.add(x)
    
    canContainTarget.remove(None)

    print(str(len(canContainTarget)) + "\n" + str(canContainTarget))
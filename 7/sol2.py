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
                mbag = re.search(r"(\d+)\s(\w+\s\w+)\sbags?", bag)
                if mbag != None and len(mbag.groups()) != 0:
                    toBags.append(mbag.group(1) + " " + mbag.group(2))
                elif "no other bags" in bag: 
                    toBags.append(None)
            #print(fromBag + " -> " + str(toBags))
            bagDict.update({fromBag: toBags})
    #print(bagDict)

    count = 0
    search = ["shiny gold"]
    while len(search) != 0:
        term = search.pop()
        item = bagDict[term]
        
        for x in item:
            if x != None:
                bag = re.search(r"(\d+)\s(\w+\s\w+)", x)
                if bag != None and len(bag.groups()) != 0:
                    #print("  got " + bag.group(1) + " " + bag.group(2))
                    count += int(bag.group(1)) 
                    for i in range(int(bag.group(1))):
                        search.append(bag.group(2))
                    print(term + " " + str(item) + " added " + bag.group(1))
                elif bag != None:
                    count += 1
                    print(term + " " + str(item) + " added 1")
    print(count)

#211 too low
#82372        

    
    
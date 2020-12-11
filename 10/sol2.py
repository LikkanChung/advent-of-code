import re

accepts = {}
highest = 0

maxloops = 0

def count(inputN):
    global maxloops
    maxloops += 1
    #print(maxloops)
    if maxloops % 1000000 == 0:
        print("progress: {:,}".format(maxloops))
    if maxloops % 1000000000000 == 0:
        if input(str(maxloops) + " continue? y/n") == "n":
            exit()

    #returns and output
    outs = accepts.get(inputN)
    #print(str(maxloops) + " === count on " + str(input) + " -> " + str(outs))
    if highest in outs:
        #print("returning 1")
        return 1
    else:
        #print("splitting at " + str(input))
        s = 0
        for out in outs:
            s += count(out)
        return s

with open('test.txt') as f:
    lines = f.read().split('\n')
    lines.append("0")
    
    num = sorted(list(map(int, lines)), reverse=True)
    

    for i in num:
        a = set()
        for j in range(i+1, i+4):
            #print(str(i) + " -> " + str(j))
            if j in num:
                a.add(j)
        #print(str(i) + " " + str(a))
        accepts.update({i: a})

    highest = num[len(num) - 1] + 3
    accepts.update({num[len(num) - 1]: {highest}})

    #print(str(count(0)))

    waysToSolve = {}
    total = 0
    for i in range(0,len(num)):
        ways = 0
        
    
    print(total)
    #waysToSolve.pop(0)
    #print(waysToSolve)

    #for n in sorted(num):

    # 215892499727278669824 too high

import re

with open('in.txt') as f:
    lines = f.read().split('\n')
    lines.append("0")
    
    num = sorted(list(map(int, lines)), reverse=True)
    
    diff = [0,0,0,1]
    for i in range(0, len(num) - 1):
        x = num[i] - num[i+1]
        print(str(num[i]) + " -> " + str(num[i+1]) + " = " + str(x))
        diff[x] += 1
    print(diff)
    print(diff[1] * diff[3])

    #1898 too low
    #1998 right
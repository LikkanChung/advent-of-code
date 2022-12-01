import re

with open('in.txt') as f:
    lines = f.read().split('\n')
    count = 0
    for line in lines:
        s = re.search(r"(\d*)-(\d*)\s([a-z]):\s([a-z]*)", line)
        first = int(s.group(1)) 
        second = int(s.group(2))
        c = s.group(3)
        p = s.group(4)

        if second <= len(line):
            if (p[first-1] == c and not p[second-1] == c) or (not p[first-1] == c and p[second-1] == c):
                count += 1
        
    print(count)        

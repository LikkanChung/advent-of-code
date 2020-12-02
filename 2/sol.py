import re

with open('in.txt') as f:
    lines = f.read().split('\n')
    count = 0
    for line in lines:
        s = re.search(r"(\d*)-(\d*)\s([a-z]):\s([a-z]*)", line)
        min = s.group(1)
        max = s.group(2)
        c = s.group(3)
        p = s.group(4)
        
        m = len(re.findall(c, p))
        if (m >= int(min) and m <= int(max)):
            count += 1
    print(count)        



        
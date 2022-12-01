import re

with open('in.txt') as f:
    lines = f.read().replace('\n\n', '~').replace('\n', ' ').split('~')
    count = 0
    for line in lines:
        group = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            print("checking " + c + " in " + line)
            if c in line:
                group += 1
        count += group
        print("##### " + str(group) + " in\n" + line + "\n#####")
    print(count)

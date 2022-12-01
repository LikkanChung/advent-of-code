import re

with open('in.txt') as f:
    lines = f.read().replace('\n\n', '~').replace('\n', ' ').split('~')

    count = 0
    for group in lines:
        everyone = group.split(' ')
        gcount = 0
        for c in "abcdefghijklmnopqrstuvwxyz":
            response = True
            for person in everyone:
                if c not in person:
                    response = False
            if response:
                gcount += 1
        count += gcount
    print(count)
import re

with open('in.txt') as f:
    lines = f.read().split('\n')

    preamble = 25
    index = preamble 
    # list refs - list[-<starts from this nth item from the back>:-<stops before this nth item from the back>]
    while index < len(lines):
        found = False
        for i in range(index - preamble, index):
            for j in range(index - preamble, index):
                if int(lines[i]) + int(lines[j]) == int(lines[index]):
                    found = True
        if not found:
            print(lines[index])
        index += 1
SHAPES = {
    'A': 'ROCK',
    'B': 'PAPER',
    'C': 'SCISSORS',
    'X': 'ROCK',
    'Y': 'PAPER',
    'Z': 'SCISSORS'
}

SCORE = {
    'ROCK': 1,
    'PAPER': 2,
    'SCISSORS': 3
}

import re

with open('2022/2/in.txt') as f:
    total = 0
    for line in f.readlines():
        if rx := re.match(r'(A|B|C) Z', line):
            # Win
            total += 6
            match rx.group(1):
                case 'A':
                    total += SCORE['PAPER']
                case 'B':
                    total += SCORE['SCISSORS']
                case 'C':
                    total += SCORE['ROCK']

        elif rx := re.match(r'(A|B|C) Y', line):
            total += 3
            total += SCORE[SHAPES[rx.group(1)]]
        else: 
            rx = re.match(r'(A|B|C) [ZYX]', line)
            match rx.group(1):
                case 'A':
                    total += SCORE['SCISSORS']
                case 'B':
                    total += SCORE['ROCK']
                case 'C':
                    total += SCORE['PAPER']
    print(total)
        

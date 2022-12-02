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
        if rx := re.match(r'(A (Y)|B (Z)|C (X))', line):
            # Win
            total += 6
        elif rx := re.match(r'(A X|B Y|C Z)', line):
            total += 3
        play = re.match(r'[ABC] (X|Y|Z)', line)
        total += SCORE[SHAPES[play.group(1)]]
    print(total)
        

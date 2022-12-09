import math
import re

FILE = '2022/9/in.txt'

def step(hx, hy, tx, ty, visited, move):
    prevhx = hx
    prevhy = hy
    print(move, ' - FROM h(', hx, hy, ') t(', tx, ty, ')')
    if move == "L": 
        hx -= 1
    elif move == "R":
        hx += 1
    elif move == "U":
        hy += 1
    elif move == "D":
        hy -= 1

    # distance hy
    distance = math.sqrt((abs(hx - tx) ** 2) + (abs(hy - ty) ** 2))
    print('   - STEP h(', hx, hy, ') t(', tx, ty, ')')
    if distance >= 2:
        tx = prevhx
        ty = prevhy

    visited.add((tx, ty))
    print('   - END  h(', hx, hy, ') t(', tx, ty, ')\n')
    return hx, hy, tx, ty, visited

with open(FILE) as f:
    hx = 0
    hy = 0
    tx = 0
    ty = 0
    visited = {(0,0)}
    rx = re.compile(r'([LRUD]) (\d+)')
    for line in f.readlines():
        move = rx.match(line)
        direction = move.group(1)
        steps = int(move.group(2))
        for i in range(steps):
            hx, hy, tx, ty, visited = step(hx, hy, tx, ty, visited, direction)

    print((visited))
    print(len(visited))

    for y in range(5, 0, -1):
        line = ''
        for x in range(6):
            line += '#' if (x, y) in visited else '.'
        print(line)

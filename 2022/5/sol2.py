import re

START = """
    [G]         [P]         [M]    
    [V]     [M] [W] [S]     [Q]    
    [N]     [N] [G] [H]     [T] [F]
    [J]     [W] [V] [Q] [W] [F] [P]
[C] [H]     [T] [T] [G] [B] [Z] [B]
[S] [W] [S] [L] [F] [B] [P] [C] [H]
[G] [M] [Q] [S] [Z] [T] [J] [D] [S]
[B] [T] [M] [B] [J] [C] [T] [G] [N]
 1   2   3   4   5   6   7   8   9 
 """

stack = [
    ['B', 'G', 'S', 'C'],
    ['T', 'M', 'W', 'H', 'J', 'N', 'V', 'G'],
    ['M', 'Q', 'S'],
    ['B', 'S', 'L', 'T', 'W', 'N', 'M'],
    ['J', 'Z', 'F', 'T', 'V', 'G', 'W', 'P'],
    ['C', 'T', 'B', 'G', 'Q', 'H', 'S'],
    ['T', 'J', 'P', 'B', 'W'],
    ['G', 'D', 'C', 'Z', 'F', 'T', 'Q', 'M'],
    ['N', 'S', 'H', 'B', 'P', 'F']
]

# stack = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

def move(count, from_stack, to_stack):
    try:
        crates = stack[from_stack - 1][-count:]
        stack[from_stack-1] = stack[from_stack-1][:-count]
        stack[to_stack - 1] = stack[to_stack -1] + crates

        for l in stack:
            print(l)
        print(from_stack, to_stack)
    except:
        raise Exception()

with open('2022/3/in.txt', 'r') as f:
    rx = re.compile(r'move (\d+) from (\d) to (\d)')
    for line in f.readlines():
        indexes = rx.match(line)
        if indexes is not None:
            count = int(indexes.group(1))
            from_stack = int(indexes.group(2))
            to_stack = int(indexes.group(3))
            # print(line, count, from_stack, to_stack)
            move(count, from_stack, to_stack)
    
    print(''.join([l[-1] for l in stack]))

with open('in.txt') as f:
    lines = f.read().split('\n')
    count = 0
    right = 1
    down = 1
    row = 0
    col = 0
    for line in lines:
        if row % down == 0:
            if (col == 0):
                c = line[0]
            else:
                c = line[col % len(line)]
            if c == '#':
                count += 1
            row += down
            col += right

    print(count)        


        
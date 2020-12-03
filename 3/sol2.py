with open('in.txt') as f:
    lines = f.read().split('\n')
    total = 1
    rights = [1,3,5,7,1]
    downs = [1,1,1,1,2]

    for x in range(len(rights)):
        row = 0
        col = 0
        count = 0
        right = rights[x]
        down = downs[x]

        while row < len(lines):
            line = lines[row]
            if row % down == 0 and row < len(lines):
                # print(str(x) + " :: row " + str(row) + " / col " + str(col))
                if (col == 0):
                    c = line[0]
                else:
                    c = line[col % len(line)]
                if c == '#':
                    count += 1
                row += down
                col += right
        total *= (count)
        print(str(x) + " " + str(right) + "r, " + str(down) + "d: " + str(count))
    print(total)

           


# 1r, 1d = 100
# 3r, 1d = 276
# 5r, 1d 
# 7r, 1d
# 1r, 2d

        
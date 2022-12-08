FILE = '2022/8/in.txt'

def get_grid(text):
    return [[int(i) for i in line.strip()] for line in text]
    # [[row1], [row2], [row3]...]
    # xy = grid[y][x]
    # 00, 01, 02, ...
    # 10, 11, 12, ...
    # 20, 21, 22, ...
    # ...

with open(FILE) as f:
    grid = get_grid(f.readlines())
    print(grid)

    # outside edge
    visible_count = 2 * (len(grid) + len(grid[0]) - 2)
    print('visible on perimeter', visible_count)

    # consider all inner trees
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            height = grid[y][x]
            visible = False
            # left, right, top, bottom views
            if max(grid[y][0:x]) < height:
                visible = True
            if max(grid[y][x+1:]) < height:
                visible = True
            if max([row[x] for row in grid[0:y]]) < height:
                visible = True
            if max([row[x] for row in grid[y+1:]]) < height:
                visible = True
            visible_count += 1 if visible else 0
            # print(x, y, visible)

    print(visible_count)
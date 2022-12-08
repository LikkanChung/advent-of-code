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
    # visible_count = 2 * (len(grid) + len(grid[0]) - 2)
    # print('visible on perimeter', visible_count)
    scores = set()
    # consider all inner trees
    for x in range(1, len(grid[0]) - 1):
        for y in range(1, len(grid) - 1):
            height = grid[y][x]
            visible = False
            # left, right, top, bottom views
            left = grid[y][0:x]
            left.reverse()
            left_score = 0
            for t in left:
                left_score += 1
                if t >= height:
                    break
            
            right = grid[y][x+1:]
            right_score = 0
            for t in right:
                right_score += 1
                if t >= height:
                    break

            top = [row[x] for row in grid[0:y]]
            top.reverse()
            top_score = 0
            for t in top:
                top_score += 1
                if t >= height:
                    break

            bottom = [row[x] for row in grid[y+1:]]
            bottom_score = 0
            for t in bottom:
                bottom_score += 1
                if t >= height:
                    break

            score = left_score * right_score * top_score * bottom_score
            scores.add(score)
            # print(x, y, score)
    
    print(max(scores))
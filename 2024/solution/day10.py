def part1(input_data):
    grid, size, trailheads = parse_input(input_data)
    print(find_paths(grid, (0, 2), 0))

def part2(input_data):
    pass

def parse_input(input_data):
    grid = [list(map(int, line.strip())) for line in input_data]
    [print(line) for line in grid]
    size = (len(grid), len(grid[0]))
    trailheads = []
    for line in range(size[0]):
        for col in range(size[1]):
            if grid[line][col] == 0:
                trailheads.append((line, col))
    return grid, size, trailheads

def find_paths(grid, pos, search_val):
    line, col = pos
    if grid[line][col] == 9:
        return [pos]
    else:
        path_branches = [
            in_bounds_pos(grid, (line - 1, col)), 
            in_bounds_pos(grid, (line, col + 1)),
            in_bounds_pos(grid, (line + 1, col)),
            in_bounds_pos(grid, (line, col - 1))
        ]
        if len(path_branches) > 0:
            return [find_paths(grid, next_pos, search_val + 1) if next_pos is not None else None for next_pos in path_branches]
        else:
            return []
        # if up/down/left/right is in bounds and equals next val then recurse call with that pos and search_val + 1
        # else dead end and return None
        # construct a list on the return, so the first call returns a list of the locations of the trail ends
        
def in_bounds_pos(grid, pos):
    return pos if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]) else None
def part1(input_data):
    pos, grid = parse_map(input_data)
    grid, _ = walk(pos, grid)
    print(sum([line.count('X') for line in grid]))
    
def part2(input_data):
    pos, grid = parse_map(input_data)
    standard_walk_grid, _ = walk(pos, grid)
    cycles = 0
    for line in range(len(standard_walk_grid)):
        for col in range(len(standard_walk_grid[line])):
            # attempt cycle if on original path
            if standard_walk_grid[line][col] == 'X' and (line, col) != pos:
                mutated_grid = grid.copy()
                mutated_grid[line] = mutated_grid[line][:col] + '#' + mutated_grid[line][col + 1:]
                _, cycle = walk(pos, mutated_grid)
                if cycle:
                    cycles += 1
    print(cycles)

def parse_map(input_data):
    starting_position = (0,0)
    for line in range(len(input_data)):
        input_data[line] = input_data[line].strip()
        if '^' in input_data[line]:
            starting_position = (line, input_data[line].index('^'))
    return starting_position, input_data

def walk(pos, grid):
    previous_visits = {}
    direction = (-1, 0) # vector
    while in_bounds(pos, grid):
        target_location = get_new_location(pos, direction)
        if not in_bounds(target_location, grid) or check_space_empty(target_location, grid):
            grid = mark_visited(pos, grid)

            if pos not in previous_visits.keys():
                previous_visits[pos] = set()
            if direction in previous_visits[pos]:
                return grid, True
            previous_visits[pos].add(direction)
            
            pos = target_location
        else:
            # rotate
            y, x = direction
            direction = (x, y * -1)
    return grid, False
            

def in_bounds(pos, grid):
    line, col = pos
    return 0 <= line < len(grid) and 0 <= col < len(grid[line])

def get_new_location(current, direction):
    current_line, current_col = current
    direction_line, direction_col = direction
    return (current_line + direction_line, current_col + direction_col)

def check_space_empty(pos, grid):
    line, col = pos
    return grid[line][col] != '#'

def mark_visited(pos, grid):
    line, col = pos
    grid_line = grid[line]
    grid[line] = grid_line[:col] + 'X' + grid_line[col + 1:]
    return grid
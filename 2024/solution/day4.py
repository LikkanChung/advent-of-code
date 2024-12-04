def part1(input_data):
    grid = input_to_array(input_data)
    find_xmas(grid, "XMAS")


def part2(input_data):
    grid = input_to_array(input_data)
    find_x_mas(grid)

def input_to_array(input_data):
    return [line.strip() for line in input_data]

def find_xmas(grid, word):
    words_found = 0
    starter_letter = word[0]
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if grid[line][col] == starter_letter:
                words_found += check_word(word, grid, (line, col), (line, col + 1), (line, col + 2), (line, col + 3)) # left to right (>)
                words_found += check_word(word, grid, (line, col), (line + 1, col), (line + 2, col), (line + 3, col)) # top to bottom (V)
                words_found += check_word(word, grid, (line, col), (line, col - 1), (line, col - 2), (line, col - 3)) # right to left (<)
                words_found += check_word(word, grid, (line, col), (line - 1, col), (line - 2, col), (line - 3, col)) # bottom to top (^)

                words_found += check_word(word, grid, (line, col), (line - 1, col + 1), (line - 2, col + 2), (line - 3, col + 3)) # up right   (./)
                words_found += check_word(word, grid, (line, col), (line + 1, col + 1), (line + 2, col + 2), (line + 3, col + 3)) # down right ('\)
                words_found += check_word(word, grid, (line, col), (line - 1, col - 1), (line - 2, col - 2), (line - 3, col - 3)) # up left    (\.)
                words_found += check_word(word, grid, (line, col), (line + 1, col - 1), (line + 2, col - 2), (line + 3, col - 3)) # down left  (/')
    print(words_found)

def find_x_mas(grid):
    x_found = 0
    starter_letter = 'A'
    word = "MAS"
    for line in range(len(grid)):
        for col in range(len(grid[line])):
            if grid[line][col] == starter_letter:
                # Left to Right MAS 
                x_found += 1 if check_word(word, grid, (line - 1, col - 1), (line, col), (line + 1, col + 1)) + check_word(word, grid, (line + 1, col - 1), (line, col), (line - 1, col + 1)) == 2 else 0
                # Top down MAS
                x_found += 1 if check_word(word, grid, (line - 1, col - 1), (line, col), (line + 1, col + 1)) + check_word(word, grid, (line - 1, col + 1), (line, col), (line + 1, col - 1)) == 2 else 0
                # Right to Left MAS
                x_found += 1 if check_word(word, grid, (line - 1, col + 1), (line, col), (line + 1, col - 1)) + check_word(word, grid, (line + 1, col + 1), (line, col), (line - 1, col - 1)) == 2 else 0
                # Bottom up MAS
                x_found += 1 if check_word(word, grid, (line + 1, col - 1), (line, col), (line - 1, col + 1)) + check_word(word, grid, (line + 1, col + 1), (line, col), (line - 1, col - 1)) == 2 else 0
    print(x_found)

def check_word(word, grid, *coords):
    width = len(grid[0])
    height = len(grid)
    return 1 if all([coor_in_bound(width, height, coord) for coord in coords]) and all([check_letter(word[i], grid, coords[i]) for i in range(len(coords))]) else 0


def coor_in_bound(width, height, coord):
    x, y = coord
    return 0 <= x < width and 0 <= y < height

def check_letter(expected, grid, coord):
    line, col = coord
    return grid[line][col] == expected

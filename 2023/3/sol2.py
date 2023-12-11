# Test2 from reddit - answer 6756, Test3 - 6756

import re

NUMBER = re.compile(r"(\d+)")
SYMBOL = re.compile(r"[^0-9\.]")

with open("2023/3/in.txt", "r") as fd: 
    lines = fd.readlines()
    width = len(lines[0])
    height = len(lines)
    numbers = {}
    gears_with_adj_nums = {}
    current_num_length = 0
    for y in range(height):
        for x in range(width):
            substring = lines[y][x:]
            number = NUMBER.match(substring)
            if current_num_length == 0:
                if number is not None:
                    extracted_number = int(number.group(1))
                    numbers[(x, y)] = extracted_number
                    current_num_length += len(number.group(1))
            current_num_length = max(current_num_length - 1, 0)

    print(str(len(numbers)) + " numbers " + str(numbers))
    for (x, y), n in numbers.items():
        search_x_min = max(x-1, 0)
        search_x_max = min(x+1+len(str(n)), width)
        search_y_min = max(y-1, 0)
        search_y_max = min(y+1, height)
        print(f"search {str(n)}: ({search_x_min},{search_y_min}) -> ({search_x_max},{search_y_max})")
        for search_line_index in range(search_y_min, min(search_y_max + 1, height)):
            sub_line = lines[search_line_index][search_x_min:search_x_max]
            print(sub_line)
            if SYMBOL.search(sub_line.strip()) is not None: 
                # print(str(n) + " OK")
                valid_search = True
                for substring_index in range(len(sub_line)):
                    if sub_line[substring_index] == '*':
                        gear_coord = (search_x_min + substring_index, search_line_index)
                        print("gear at " + str(gear_coord))
                        if gears_with_adj_nums.get(gear_coord) is None:
                            gears_with_adj_nums[gear_coord] = [n]
                        else:
                            gears_with_adj_nums[gear_coord].append(n)
                
    print(gears_with_adj_nums)
    sum = 0
    for part_numbers in gears_with_adj_nums.values():
        if len(part_numbers) == 2:
            sum += part_numbers[0] * part_numbers[1]
    print("total " + str(sum))
    # print("invalid " + str(set(numbers.values()).difference(valid_numbers)))
    

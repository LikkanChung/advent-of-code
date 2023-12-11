# Test2 from reddit - answer 413, Test3 - 925
# https://www.reddit.com/r/adventofcode/comments/189q9wv/comment/kbsrno0/?utm_source=share&utm_medium=web2x&context=3

import re

NUMBER = re.compile(r"(\d+)")
SYMBOL = re.compile(r"[^0-9\.]")

with open("2023/3/in.txt", "r") as fd: 
    lines = fd.readlines()
    width = len(lines[0])
    height = len(lines)
    numbers = {}
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

    sum = 0
    # print(str(len(numbers)) + " numbers " + str(numbers))
    for (x, y), n in numbers.items():
        search_x_min = max(x-1, 0)
        search_x_max = min(x+1+len(str(n)), width)
        search_y_min = max(y-1, 0)
        search_y_max = min(y+1, height)
        valid_search = False
        for search_line in lines[search_y_min:search_y_max + 1]:
            sub_line = search_line[search_x_min:search_x_max]
            # if n == 533:
            #     print(sub_line)
            if SYMBOL.search(sub_line.strip()) is not None: 
                # print(str(n) + " OK")
                valid_search = True
        if n == 790:
            print(valid_search)
        if valid_search:
            sum += n
    print("total " + str(sum))
    # print("invalid " + str(set(numbers.values()).difference(valid_numbers)))
    

import bisect

def part1(input_data):
    left_numbers, right_numbers = parse_input(input_data)

    sum = 0
    for i in range(len(input_data)):
        left = left_numbers[i]
        right = right_numbers[i]
        sum += get_distance(left, right)
    print(sum)


def part2(input_data):
    left_numbers, right_numbers = parse_input(input_data)
    right_frequency = count_frequency(right_numbers)
    sum = 0
    for left in left_numbers:
        sum += int(left) * right_frequency.get(int(left), 0)
    print(sum)

def parse_input_line(line):
    line_parts = line.split("   ", 2)
    left = line_parts[0].strip()
    right = line_parts[1].strip()
    return (left, right)

def parse_input(input_data):
    left_numbers = []
    right_numbers = []
    for line in input_data:
        left, right = parse_input_line(line)
        bisect.insort(left_numbers, left)
        bisect.insort(right_numbers, right)
    return (left_numbers, right_numbers)

def get_distance(x, y):
    return abs(int(x) - int(y))
        
def count_frequency(number_list):
    frequencies = {}
    for num in number_list:
        num = int(num)
        if num not in frequencies:
            frequencies[num] = 1
        else:
            frequencies[num] += 1
    return frequencies
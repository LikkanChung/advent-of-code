import re

re_equation = re.compile(r"(\d+): ([\d ]+)")

def part1(input_data):
    print(sum([target if check_equations(target, None, numbers) else 0 for target, numbers in parse_input(input_data)]))
        
def part2(input_data):
    print(sum([target if check_equations_concat(target, None, numbers) else 0 for target, numbers in parse_input(input_data)]))

def parse_input(input_data):
    inputs = []
    for line in input_data:
        target, numbers = re_equation.search(line).groups()
        inputs.append((int(target), list(map(int, numbers.split(' ')))))
    return inputs

def check_equations(target, accumulator, numbers):
    if len(numbers) == 0:
        return target == accumulator
    elif accumulator == None:
        return check_equations(target, numbers[0], numbers[1:])
    else:
        return check_equations(target, accumulator + numbers[0], numbers[1:]) or check_equations(target, accumulator * numbers[0], numbers[1:])
    
def check_equations_concat(target, accumulator, numbers):
    if len(numbers) == 0:
        return target == accumulator
    elif accumulator == None:
        return check_equations_concat(target, numbers[0], numbers[1:])
    else:
        return check_equations_concat(target, accumulator + numbers[0], numbers[1:]) \
            or check_equations_concat(target, accumulator * numbers[0], numbers[1:]) \
            or check_equations_concat(target, int(str(accumulator) + str(numbers[0])), numbers[1:])
 
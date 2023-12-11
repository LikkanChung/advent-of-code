import re
import random

def get_number(line: str):
    digits = re.sub(r"[^0-9]", "", line)
    return int(str(digits[0]) + str(digits[-1]))

def replace_alpha_digits(line: str):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(line)):
        substring = line[0:i]
        for j in range(10):
            if re.search(numbers[j], substring) is not None:
                line = substring[0:1] + re.sub(numbers[j], str(j), substring) + line[i-1:]
    return line


def process_line(line: str):
    if random.choice([True, False]) == True:
        print("--------")
        print(line.strip("\n"))
        line = get_number(replace_alpha_digits(line))
        print(line)
    else: 
        line = get_number(replace_alpha_digits(line))
    return line
                      
                    
with open("2023/1/in.txt", "r") as fd: 
    lines = fd.readlines()
    total = sum([process_line(l) for l in lines])
    print(total)
import re

def part1(input_data):
    re_mul = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    print(sum([x * y for (x, y) in [(int(x), int(y)) for (x, y) in re_mul.findall("".join(input_data))]]))

def part2(input_data):
    re_conditional_mul = re.compile(r"(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    input_data = "".join(input_data)
    matches = re_conditional_mul.findall(input_data)
    include = True
    sum = 0
    for match in matches:
        do, dont, x, y = match
        if do != "":
            include = True
        elif dont != "":
            include = False
        elif include == True:
            sum += int(x) * int(y)
    print(sum)

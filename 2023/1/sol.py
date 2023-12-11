import re

def get_number(line: str):
    digits = re.sub(r"[^0-9]", "", line)
    return int(str(digits[0]) + str(digits[-1]))

with open("2023/1/in.txt", "r") as fd: 
    lines = fd.readlines()
    total = sum([get_number(l) for l in lines])
    print(total)
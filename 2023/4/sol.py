import re

CARD = re.compile(r"Card\s+(\d+):\s+([\d\s]+) \|\s+([\d\s]+)")

def get_score(winning_numbers_str: str, played_numbers_str: str):
    winning_numbers = set(map(lambda n: int(n) , winning_numbers_str.replace("  ", " ").split(" ")))
    played_numbers = set(map(lambda n: int(n), played_numbers_str.replace("  ", " ").split(" ")))
    win = winning_numbers.intersection(played_numbers)
    if len(win) > 0:
        return pow(2, len(win) - 1)
    else: 
        return 0

def get_card_score(line: str):
    match = CARD.match(line)
    if match is not None:
        # print(line)
        return get_score(match.group(2), match.group(3))
    else: 
        print("NON MATCH " + line)

with open("2023/4/test.txt", "r") as fd: 
    lines = fd.readlines()
    print(sum([get_card_score(line) for line in lines]))
        
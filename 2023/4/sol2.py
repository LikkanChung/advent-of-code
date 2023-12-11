import re

CARD = re.compile(r"Card\s+(\d+):\s+([\d\s]+) \|\s+([\d\s]+)")

def get_matches(winning_numbers_str: str, played_numbers_str: str):
    winning_numbers = set(map(lambda n: int(n) , winning_numbers_str.replace("  ", " ").split(" ")))
    played_numbers = set(map(lambda n: int(n), played_numbers_str.replace("  ", " ").split(" ")))
    win = winning_numbers.intersection(played_numbers)
    # if len(win) > 0:
    #     return pow(2, len(win) - 1)
    # else: 
    #     return 0
    return len(win)

def get_card_matches(line: str):
    match = CARD.match(line)
    if match is not None:
        # print(line)
        return get_matches(match.group(2), match.group(3))
    else: 
        print("NON MATCH " + line)


def count_copies(card_number, lines):
    print("counting " + (str(card_number)))
    score = 0
    expand_to_next = get_card_matches(lines[card_number - 1])
    print("expanding " + str(expand_to_next))
    score += 1
    if expand_to_next != 0:
        print("next cards ")
        # [print(line) for line in lines[card_number: card_number + expand_to_next]]
        score += sum([count_copies(n, lines) for n in range(card_number + 1, card_number + 1 + expand_to_next)])
    return score


with open("2023/4/in.txt", "r") as fd: 
    lines = fd.readlines()
    print(sum([count_copies(i+1, lines) for i in range(len(lines))]))
        
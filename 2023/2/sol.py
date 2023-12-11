import re

GAME_PATTERN = re.compile(r"Game (\d+): (([0-9a-z,\s]+;?)*)")
CUBE_PATTERN = re.compile("(\d+) (red|green|blue)")

LIMIT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def validate_colour_set(cube_set):
    set_record = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for cube_colour in cube_set.split(", "):
        colour_match = CUBE_PATTERN.search(cube_colour)
        if colour_match is not None:
            number = colour_match.group(1)
            colour = colour_match.group(2)
            set_record[colour] =+ int(number)
    if all([set_record.get(col) <= LIMIT.get(col) for col in set_record.keys()]):
        return True


with open("2023/2/in.txt", "r") as fd: 
    lines = fd.readlines()
    total = 0
    for line in lines: 
        match = GAME_PATTERN.search(line)
        if match is not None:
            game_number = match.group(1)
            game_record = match.group(2)
            # print(game_number + ": " + game_record)
            if all([validate_colour_set(cube_set) for cube_set in game_record.split("; ")]):
                print("Valid game " + game_number)
                total += int(game_number)

    print(total)
            
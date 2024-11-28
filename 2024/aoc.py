import sys
import os
import shutil
import argparse

USAGE = """
Advent of Code Utility:
To start a new day:
 > python aoc.py init <day>
 Where <day> is the calendar day (1, 2, ... 25)
 This will create the tempate solution file and test/real data files 

To test a solution:
 > python aoc.py solve <day> -p=<part> [-t]
 Where <part> is either `1` or `2`
 If `-t` or `--test` flag is used then the solution is tested with the test data set, otherwise the real data is used
"""

def init(day: str, real_data_dir: str, test_data_dir: str, solution_dir: str, template_file: str):
    print(f"Initialising Day {day} solution files")
    open(os.path.join(real_data_dir, f"day{day}.txt"), "a+")
    open(os.path.join(test_data_dir, f"day{day}.txt"), "a+")
    if not os.path.exists(os.path.join(solution_dir, f"day{day}.py")):
        shutil.copyfile(
            os.path.join(solution_dir, template_file),
            os.path.join(solution_dir, f"day{day}.py")
        )
    

def solve(day: str, part: str, data_dir: str):
    print(f"Solving Day {day} part {part} with {data_dir} data")
    
    module_name = f"solution.day{day}"
    module = __import__(module_name, fromlist=[''])

    data_file = os.path.join(data_dir, f"day{day}.txt")
    data = open(data_file, "r").readlines() 

    if part == "1":
        module.part1(data)
    elif part == "2":
        module.part2(data)
    else:
        print("Error: Solution must be part 1 or 2")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("utility", help="'init' the day or 'solve'")
    parser.add_argument("day", help="The Day number between 1 and 25")
    parser.add_argument("-p", "--part", help="The part to solve, `1` or `2`. Calls the `partX` function in the day's solution")
    parser.add_argument("-t", "--test", action="store_true", help="Use the test data set instead of solving for the real solution")
    args = parser.parse_args()

    UTILITY = args.utility # init or solve
    DAY = args.day # 1 to 25

    TEST_DATA_DIR = "test-input"
    REAL_DATA_DIR = "input"
    SOLUTION_DIR = "solution"
    TEMPLATE_SOLUTION = "template.py"

    if UTILITY == "init":
        init(DAY, REAL_DATA_DIR, TEST_DATA_DIR, SOLUTION_DIR, TEMPLATE_SOLUTION)
    elif UTILITY == "solve": 
        PART = args.part # 1 or 2
        DATA_DIR = TEST_DATA_DIR if args.test else REAL_DATA_DIR
        solve(DAY, PART, DATA_DIR)
    else:
        print("Error: argument must be init or solve")

if __name__ == "__main__":
    main()


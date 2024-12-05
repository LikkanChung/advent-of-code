import re
import random
import functools

re_input = re.compile(r"(\d+)\|(\d+)|([\d,\s]+)")

def part1(input_data):
    order_rules, print_pages = parse_input(input_data)
    print(sum([update[int(len(update) / 2)] if check_valid_order(update, order_rules) else 0 for update in print_pages]))

def part2(input_data):
    order_rules, print_pages = parse_input(input_data)
    print(sum([order_correctly(update, order_rules)[int(len(update) / 2)] if not check_valid_order(update, order_rules) else 0 for update in print_pages]))

def parse_input(input_data):
    order_rules = {} # key = page number, val = these pages must follow page number
    print_pages = []
    for line in input_data:
        match = re_input.match(line.strip())

        if match is not None:
            n1, n2, pages = match.groups()
            if n1 and n2:
                n1 = int(n1)
                n2 = int(n2)
                if n1 not in order_rules.keys():
                    order_rules[n1] = [n2]
                else:
                    order_rules[n1].append(n2)
            else:
                print_pages.append([int(x) for x in pages.split(",")])
    return order_rules, print_pages

def check_valid_order(update, order_rules):
    valid = True
    for i in range(len(update)):
        # rules is a dict of k:v - k must be before all v, 
        # so if any of the numbers before k in the update list are members of list v then it's bad
        target_rule = update[i]
        check_numbers = update[:i]
        disallowed_numbers = order_rules.get(target_rule) or []
        if check_rule_breaks(check_numbers, disallowed_numbers):
            valid = False
    return valid

def check_rule_breaks(actual_list, disallowed_numbers):
    return any([n in disallowed_numbers for n in actual_list])

def order_correctly(update, order_rules):
    return sorted(update, key=functools.cmp_to_key(comparator(order_rules)))


def comparator(order_rules):
    def compare(x, y):
        following_numbers = order_rules.get(x) or [] 
        return -1 if y in following_numbers else 1
    return compare
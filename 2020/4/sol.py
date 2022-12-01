import re

with open('in.txt') as f:
    lines = f.read().replace('\n\n', '~').replace('\n', ' ').split('~')
    count = 0
    for line in lines:
        if len(re.findall('byr:', line)) != 0:
            if len(re.findall('iyr:', line)) != 0:
                if len(re.findall('eyr:', line)) != 0:
                    if len(re.findall('hgt:', line)) != 0:
                        if len(re.findall('hcl:', line)) != 0:
                            if len(re.findall('ecl:', line)) != 0:
                                if len(re.findall('pid:', line)) != 0:
                                    count += 1
    print(count)

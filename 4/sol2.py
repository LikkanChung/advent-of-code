import re

with open('in.txt') as f:
    lines = f.read().replace('\n\n', '~').replace('\n', ' ').split('~')
    count = 0
    lc = 0
    for line in lines:
        match = re.search(r"(byr):(\d{4})", line)
        if match != None and len(match.groups()) != 0 and int(match.group(2)) >= 1920 and int(match.group(2)) <= 2002:
            match = re.search(r"(iyr):(\d{4})", line)
            if match != None and len(match.groups()) != 0 and int(match.group(2)) >= 2010 and int(match.group(2)) <= 2020:
                match = re.search(r"(eyr):(\d{4})", line)
                if match != None and len(match.groups()) != 0 and int(match.group(2)) >= 2020 and int(match.group(2)) <= 2030:
                    match = re.search(r"(hgt):(\d+)(cm|in)", line)
                    if match != None and len(match.groups()) != 0:
                        if ((match.group(3) == "cm" and int(match.group(2)) >= 150 and int(match.group(2)) <= 193) or (match.group(3) == "in" and int(match.group(2)) >= 59 and int(match.group(2)) <= 76)):
                            match = re.search(r"(hcl):\#([0-9a-f]{6}[^0-9a-f]*)", line)
                            if match != None and len(match.groups()) != 0:
                                match = re.search(r"(ecl):(amb|blu|brn|gry|grn|hzl|oth)", line)
                                if match != None and len(match.groups()) != 0:
                                    match = re.search(r"(pid):(\d{9})", line) # this matches 1 too many cases where pid is 10 digits.
                                    if match != None and len(match.groups()) != 0:
                                        count += 1
                                        print(str(lc) + "                           MATCH " + str(count) + ": " + str(line))
                                    else:
                                        if match != None:
                                            print(str(lc) + " rejected on pid = " + match.group(2) + " from " + line)
                                        else: print(str(lc) + " rejected missing pid from" + line)
                                else: 
                                    if match != None:
                                        print(str(lc) + " rejected on ecl = " + match.group(2) + " from " + line)
                                    else: print(str(lc) + " rejected missing ecl from " + line)
                            else:
                                if match != None:
                                    print(str(lc) + " rejected on hcl = " + match.group(2) + " from " + line)
                                else: print(str(lc) + " rejected missing hcl from " + line)
                        else: 
                            if match != None:
                                print(str(lc) + " rejected on hgt = " + match.group(2) + " " + match.group(3) + " from " + line)
                            else: print(str(lc) + " rejected missing hgt from " + line)
                    else: 
                        if match != None:
                            print(str(lc) + " rejected on hgt not matched from " + line)
                        else: print(str(lc) + " rejected missing hgt from " + line)
                else:
                    if match != None:
                        print(str(lc) + " rejected on eyr = " + match.group(2) + " from " + line)
                    else: print(str(lc) + " rejected missing eyr from " + line)
            else:
                if match != None:
                    print(str(lc) + " rejected on iyr = " + match.group(2) + " from " + line)
                else: print(str(lc) + " rejected missing iyr from " + line)
        else:
            if match != None:
                print(str(lc) + " rejected on byr = " + match.group(2) + " from " + line)
            else: print(str(lc) + " rejected missing byr from " + line)
        lc += 1
                
    print(count)

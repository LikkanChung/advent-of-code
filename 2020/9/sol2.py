import re

with open('in.txt') as f:
    lines = f.read().split('\n')

    # preamble = 25
    # index = preamble 
    # # list refs - list[-<starts from this nth item from the back>:-<stops before this nth item from the back>]
    # while index < len(lines):
    #     found = False
    #     for i in range(index - preamble, index):
    #         for j in range(index - preamble, index):
    #             if int(lines[i]) + int(lines[j]) == int(lines[index]):
    #                 found = True
    #     if not found:
    #         print(lines[index])
    #     index += 1

    target = 1721308972
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            # range 
            #print(str(i) + " " + str(j))
            count = 0
            min = int(lines[len(lines)-1])
            max = int(lines[0])
            numlist = []
            for k in lines[i: j]:
                count += int(k)
                numlist.append(int(k))
                if int(k) < min:
                    min = int(k)
                if int(k) > max:
                    max = int(k)
            if count == target:
                print(str(min) + " + " + str(max) + " = " + str(min + max) + " from " + str(numlist) + " E=" + str(sum(numlist)))
                #188477775 too low
                #137282723 nope
                #1721308976 too high
                #3969111208 too high
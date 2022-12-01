import re

with open('in.txt') as f:
    lines = f.read().split('\n')
    
    count = []
    for x in lines:
        count.append(0)

    acc = 0
    index = 0

    while (count[index] == 0):
        command = lines[index]
        num = re.search(r"([+-]\d+)", command).group(1)
        print("### " + command)
        if "acc" in command:
            print(str(index) + " acc " + num)
            acc += int(num)
            index += 1
        elif "jmp" in command:
            print(str(index) + " jmp " + num)
            index += int(num)
        elif "nop" in command:
            print(str(index) + " nop " + num)
            index += 1
        count[index-1] += 1
    print(acc)
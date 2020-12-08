import re

def run(inlines, swapindex) :
    acc = 0
    index = 0
    count = []
    for i in range(len(lines)):
        count.append(0)
    while (index < len(inlines) and count[index] == 0):
        command = inlines[index]
        num = re.search(r"([+-]\d+)", command).group(1)
        if index == swapindex:
            if "jmp" in command:
                command = "nop " + str(num)
            elif "nop" in command:
                command = "jmp " + str(num)
        if "acc" in command:
            #print(str(index) + " acc " + num)
            acc += int(num)
            index += 1
        elif "jmp" in command:
            #print(str(index) + " jmp " + num)
            index += int(num)
        elif "nop" in command:
            #print(str(index) + " nop " + num)
            index += 1
        count[index-1] += 1
        if index == len(inlines): 
            print("#############")
    return str(index) + " " + str(acc)

with open('in.txt') as f:
    lines = f.read().split('\n')
    for i in range(len(lines)):
        if "jmp" in lines[i] or "nop" in lines[i]:
            print(run(lines, i))

#1832 too high    
#662
    

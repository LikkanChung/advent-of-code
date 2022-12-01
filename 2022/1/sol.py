FILE = '2022/1/in.txt'

with open(FILE, 'r') as numbers: 
    largest = 0
    sum = 0
    for line in numbers.readlines():
        if line == '\n':
            largest = max(largest, sum)
            sum = 0
        else: 
            sum += int(line)
    print(largest)
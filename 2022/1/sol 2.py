FILE = '2022/1/in.txt'

with open(FILE, 'r') as numbers: 
    totals = []
    sum = 0
    for line in numbers.readlines():
        if line == '\n':
            totals.append(sum)
            sum = 0
        else: 
            sum += int(line)
    
    totals.sort(reverse=True)

    print(totals[0] + totals[1] + totals[2])
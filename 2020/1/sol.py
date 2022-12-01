with open('in.txt') as f:
    lines = f.read().split('\n')
    for x in lines:
        for y in lines:
            if int(x) + int(y) == 2020:
                print(int(x) * int(y))


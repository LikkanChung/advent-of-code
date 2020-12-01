with open('in.txt') as f:
    lines = f.read().split('\n')
    for x in lines:
        if int(x) < 2020:
            for y in lines:
                if int(x) + int(y) < 2020:
                    for z in lines:
                        if int(x) + int(y) + int(z) == 2020:
                            print(int(x) * int(y) * int(z))


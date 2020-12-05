def half(low, high, x):
    #print (str(low) + " " + str(high) + " " + x + " --> ")
    if x == 'F' or x == 'L':
        # front or left or lower        
        #print(str(low) + " " + str(int((high + low)/2)))
        return (low, int((high + low)/2))
    else:
        #print(str(int((high  + low)/2) + 1) + " " + str(high))
        return (int((high + low)/2) + 1, high)
    

with open('in.txt') as f:
    lines = f.read().split('\n')
    low = 0
    high = 127
    left = 0
    right = 7

    id = 0
    count = 0

    # empty array
    init = '.'
    seats = []
    row = []
    for x in range(0, high + 1):
        for y in range (0, right + 1):
            row.append(init)
        seats.append(row)
        row = []
    
    #lines = [lines[837]]
    foundlist = []

    for line in lines:
        rlow = low
        rhigh = high
        rleft = left
        rright = right
        for i in range(7):
            (rlow, rhigh) = half(rlow, rhigh, line[i])
            if rlow == rhigh:
                for j in range (7, 10):
                    #print(" half on " + line[j] + " with " + str(rleft) + " " + str(rright))
                    (rleft, rright) = half(rleft, rright, line[j])
                    if rleft == rright:
                        m = (rhigh * 8) + rright
                        if m > id:
                            id = m
                        seats[rhigh][rright] = 'X'
                        print(str(count) + " : seat " + str(rhigh) + " " + str(rright) + " id" + str(m) + " from " + line)
                        foundlist.append(m)
                #print("err: " + line + str(rlow) + " " + str(r))
        #print(line + " " + str(rlow) + " " + str(rhigh))
        count += 1
    
    # build out
    index = 0
    for r in seats:
        rowline = str("{:4s}".format(str(index))) + " " 
        for x in r:
            rowline += x
        print(rowline)
        index += 1

    # tests
    # for i in range(0,128):
    #     for j in range(0,8):
    #         if (i * 8) + j not in foundlist:
    #             print("MISSING id " + str((i*8)+j) + " from " + str(i) + " " + str(j))


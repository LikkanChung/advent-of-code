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
    
    #lines = [lines[0]]

    for line in lines:
        rlow = low
        rhigh = high
        rleft = left
        rright = right
        for i in range(7):
            (rlow, rhigh) = half(rlow, rhigh, line[i])
            if rlow == rhigh:
                for j in range (5, 8):
                    (rleft, rright) = half(rleft, rright, line[i])
                    if rleft == rright:
                        m = (rhigh * 8) + rright
                        if m > id:
                            id = m
            
                #print("err: " + line + str(rlow) + " " + str(r))
        #print(line + " " + str(rlow) + " " + str(rhigh))
    print(id)


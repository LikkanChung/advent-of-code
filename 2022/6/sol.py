with open('2022/6/in.txt') as f:
    header_len = 14  # part 1 = 4, part 2 = 14
    text = f.readlines()[5]
    # tests: 0 = 7, 1 = 5, 2 = 6, 3 = 10, 4 = 11
    # problem: 5 = ???
    count = len(text)
    print(count)
    for i in range(count):
        print(str(i) + ':' + str(min(1+header_len,count)) + ' ' + text[i:min(1+header_len, count)] + ' ' +  str(set(text[i:min(i+header_len,count)])))
        if len(set(text[i:min(i+header_len,count)])) == header_len:
            print(i+header_len)
            break
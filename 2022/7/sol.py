import re


FILE = '2022/7/in.txt'
cd = re.compile(r'\$ cd (.*)')
ls = re.compile(r'\$ ls')
ls_out = re.compile(r'(\w+) (.+)')

def parse_log(lines,):
    current_dir = []
    parse_tree = {}

    output_expected = False
    for line in lines:
        if cd_rx := cd.match(line):
            # print(cd_rx.groups())
            dir = cd_rx.group(1)
            if dir == '/':
                current_dir = ['/']
            elif dir == '..':
                current_dir.pop()
            else:
                current_dir.append(dir)
            output_expected = False
        elif ls_rx := ls.match(line):
            output_expected = True
        elif ls_out_rx := ls_out.match(line):
            size_or_type = ls_out_rx.group(1)
            name = ls_out_rx.group(2)

            target = parse_tree
            for sub_dir in current_dir:
                if target.get(sub_dir) is None:
                    target[sub_dir] = {}
                target = target[sub_dir]
            
            if size_or_type == 'dir':
                target[name] = {}
            else:
                target[name] = int(size_or_type)
        else:
            print('no rx match on ' + line)
    
        print(parse_tree)
    return parse_tree
            

def dir_size(tree):
    size = 0
    for item in tree:
        if type(tree[item]) is dict:
            size += dir_size(tree[item])
        else:
            size += tree[item]
    return size


def find_sizes(tree, sizes):
    # ignores / - assuming it's always too big

    for item in tree:

        size_of_dir = 0
        if type(tree[item]) is dict:
            size_of_dir = dir_size(tree[item])
            find_sizes(tree[item], sizes)
        #if size_of_dir <= 100000:
            sizes.append(size_of_dir)
    return sizes
        


with open(FILE) as f:
    tree = parse_log(f.readlines())
    print('parsing')
    sizes = find_sizes(tree, [])
    print(sizes)
    print('part 1', sum([i if i <= 100000 else 0 for i in sizes]))

    total_space = 70000000
    required_space = 30000000
    used_space = dir_size(tree)
    unused_space = total_space - used_space
    minimum_deletion = required_space - unused_space
    print('min deletion', minimum_deletion)
    sizes.sort()
    for size in sizes:
        if size > minimum_deletion:
            print('part 2', size)
            break







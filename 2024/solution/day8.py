def part1(input_data):
    grid, size, locations = pasrse_input(input_data)
    antinodes = set()
    for key, freq_list in locations.items():
        print(key)
        for i in range(len(freq_list)):
            source_loc = freq_list[i]
            other_locs = freq_list[:i] + freq_list[i+1:]
            for other_loc in other_locs:
                vector = get_vector(source_loc, other_loc)
                antinode = get_antinode(other_loc, vector)
                if in_bounds(size, antinode):
                    antinodes.add(antinode)

    print(len(antinodes))

def part2(input_data):
    grid, size, locations = pasrse_input(input_data)
    antinodes = set()
    for key, freq_list in locations.items():
        for i in range(len(freq_list)):
            source_loc = freq_list[i]
            other_locs = freq_list[:i] + freq_list[i+1:]
            for other_loc in other_locs:
                target_loc = other_loc
                reached_out_of_bounds = False
                vector = get_vector(source_loc, other_loc)
                antinodes.add(other_loc)
                while not reached_out_of_bounds:
                    antinode = get_antinode(target_loc, vector)
                    if in_bounds(size, antinode):
                        antinodes.add(antinode) 
                        target_loc = antinode
                    else:
                        reached_out_of_bounds = True
    print(len(antinodes))


def pasrse_input(input_data):
    data = [line.strip() for line in input_data]
    size = (len(data), len(data[0]))
    locations = {}
    for line in range(size[0]):
        for col in range(size[1]):
            antenna = data[line][col]
            if antenna != '.':
                if antenna not in locations.keys():
                    locations[antenna] = [(line, col)]
                else:
                    locations[antenna].append((line, col))
    return data, size, locations

def get_vector(loc1, loc2):
    return (loc2[0] - loc1[0], loc2[1] - loc1[1])

def get_antinode(loc, vector):
    return (loc[0] + vector[0], loc[1] + vector[1])

def in_bounds(size, loc):
    return 0 <= loc[0] < size[0] and 0 <= loc[1] < size[1]
import re

SEEDS_RE = re.compile(r"seeds: ([\d\s]+)")

input_vals = {
    "file": "2023/5/in.txt",
    "seeds_line": 0,
    "seed_soil": {
        "start": 3,
        "end": 15
    },
    "soil_fertilizer": {
        "start": 17,
        "end": 46
    },
    "fertilizer_water": {
        "start": 48,
        "end": 65
    },
    "water_light": {
        "start": 67,
        "end": 85
    },
    "light_temperature": {
        "start": 87,
        "end": 121
    },
    "temperature_humidity": {
        "start": 123,
        "end": 157
    },
    "humidity_location": {
        "start": 160,
        "end": 172
    }
}

# input_vals = {
#     "file": "2023/5/test.txt",
#     "seeds_line": 0,
#     "seed_soil": {
#         "start": 3,
#         "end": 5
#     },
#     "soil_fertilizer": {
#         "start": 7,
#         "end": 10
#     },
#     "fertilizer_water": {
#         "start": 12,
#         "end": 16
#     },
#     "water_light": {
#         "start": 18,
#         "end": 20
#     },
#     "light_temperature": {
#         "start": 22,
#         "end": 25
#     },
#     "temperature_humidity": {
#         "start": 27,
#         "end": 29
#     },
#     "humidity_location": {
#         "start": 31,
#         "end": 33
#     }
# }

def process_map_lines(lines: list[str]):
    # mapping = {}
    # for line in lines:
    #     line_values = line.strip().split(" ")
    #     range_length = range(int(line_values[2]))
    #     source_start = int(line_values[1])
    #     destination_start = int(line_values[0])
    #     for i in range_length:
    #         mapping[source_start + i] = destination_start + i
    # return mapping
    mappings = []
    for line in lines:
            line_values = line.strip().split(" ")
            range_length = int(line_values[2])
            source_start = int(line_values[1])
            destination_start = int(line_values[0])
            entry = {
                 "source": {
                      "start": source_start,
                      "end": source_start + range_length - 1
                 },
                 "destination": destination_start
            }
            mappings.append(entry)
    return mappings


def get_mapping(key: int, maps: list):
    # if key in map.keys():
    #     return map.get(key)
    # else: 
    #     return key
    for map in maps:
        if key >= map.get("source").get("start") and key <= map.get("source").get("end"):
              offset = key - map.get("source").get("start")
              return map.get("destination") + offset
    return key

def get_seeds(line):
    seeds = set()
    values = SEEDS_RE.match(lines[input_vals.get("seeds_line")]).group(1).split(" ")
    print(values)
    for i in range(0, len(values), 2):
        print(i)
        for r in range(int(values[i+1])):
             seeds.add(int(values[i])+r)
    return seeds


with open(input_vals.get("file"), "r") as fd:
    lines = [l.strip() for l in fd.readlines()]
    # seeds = set(map(lambda x: int(x), SEEDS_RE.match(lines[input_vals.get("seeds_line")]).group(1).split(" ")))
    seeds = get_seeds(lines[input_vals.get("seeds_line")])
    print(seeds)

    print("Starting mapping seed_soil")
    seeds_soil_map_lines = lines[input_vals.get("seed_soil").get("start"): input_vals.get("seed_soil").get("end")]
    seeds_soil_map = process_map_lines(seeds_soil_map_lines)
    
    print("Starting mapping soil_fertilizer")
    soil_fertilizer_map = process_map_lines(lines[input_vals.get("soil_fertilizer").get("start"): input_vals.get("soil_fertilizer").get("end")])
    
    print("Starting mapping fertilizer_water")
    fertilizer_water_map = process_map_lines(lines[input_vals.get("fertilizer_water").get("start"): input_vals.get("fertilizer_water").get("end")])

    print("Starting mapping water_light")
    water_light_map = process_map_lines(lines[input_vals.get("water_light").get("start"): input_vals.get("water_light").get("end")])

    print("Starting mapping light_temperature")
    light_temperature_map = process_map_lines(lines[input_vals.get("light_temperature").get("start"): input_vals.get("light_temperature").get("end")])

    print("Starting mapping temperature_humidity")
    temperature_humidity_map = process_map_lines(lines[input_vals.get("temperature_humidity").get("start"): input_vals.get("temperature_humidity").get("end")])

    print("Starting mapping humidity_location")
    humidity_location_map = process_map_lines(lines[input_vals.get("humidity_location").get("start"): input_vals.get("humidity_location").get("end")])

    print("Mapping Complete")
    
    # for seed in seeds:
    #     soil = get_mapping(seed, seeds_soil_map)
    #     fertilizer = get_mapping(soil, soil_fertilizer_map)

    #     location = get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(seed, seeds_soil_map), soil_fertilizer_map), fertilizer_water_map), water_light_map), light_temperature_map), temperature_humidity_map), humidity_location_map)
        
    #     print(f"seed {str(seed)} {str(soil)} {str(fertilizer)} ... {location}")

    print(min([get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(get_mapping(seed, seeds_soil_map), soil_fertilizer_map), fertilizer_water_map), water_light_map), light_temperature_map), temperature_humidity_map), humidity_location_map) for seed in seeds]))
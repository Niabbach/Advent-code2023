seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

map_lists = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light,
             light_to_temperature, temperature_to_humidity, humidity_to_location]

with open('input5.txt', 'r') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith('seeds:'):
            seeds = [int(x) for x in line.split()[1:]]
            continue
        elif line.startswith('seed-to-soil'):
            map_list = seed_to_soil
            continue
        elif line.startswith('soil-to-fertilizer'):
            map_list = soil_to_fertilizer
            continue
        elif line.startswith('fertilizer-to-water'):
            map_list = fertilizer_to_water
            continue
        elif line.startswith('water-to-light'):
            map_list = water_to_light
            continue
        elif line.startswith('light-to-temperature'):
            map_list = light_to_temperature
            continue
        elif line.startswith('temperature-to-humidity'):
            map_list = temperature_to_humidity
            continue
        elif line.startswith('humidity-to-location'):
            map_list = humidity_to_location
            continue
        temp = [int(x) for x in line.split()]
        map_list.append((temp[1], temp[2], temp[0]))

def get_dest(src, map_list):
    for s, r, d in map_list:
        if s <= src < s+r:
            return src - s + d
    return src


def get_location(seed):
    temp = seed
    for map_list in map_lists:
        temp = get_dest(temp, map_list)
    return temp

# part 1
print(min(get_location(seed) for seed in seeds))

# part 2
seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i]+seeds[i+1]-1))
print(seed_ranges)

def get_ranges(src_ranges, map_list):
    result = []
    for a, b in src_ranges:
        covered_ranges = []
        for s, r, d in map_list:
            x, y = s, s+r-1
            if b < x or y < a:
                continue
            inter1 = max(a, x)
            inter2 = min(b, y)
            covered_ranges.append((inter1, inter2))
            result.append((inter1-s+d, inter2-s+d))
        # now check for all sections of range left uncovered
        if not covered_ranges:
            result.append((a, b))
            continue
        covered_ranges.sort()
        # check beginning
        if covered_ranges[0][0] > a:
            result.append((a, covered_ranges[0][0]-1))
        # check end
        if covered_ranges[-1][1] < b:
            result.append((covered_ranges[-1][1]+1, b))
        for i in range(len(covered_ranges)-1):
            x1, y1 = covered_ranges[i]
            x2, y2 = covered_ranges[i+1]
            if x2 > y1+1:
                result.append((y1+1, x2-1))
    return result
def get_location_ranges(seed_ranges):
    temp = seed_ranges
    for map_list in map_lists:
        temp = get_ranges(temp, map_list)
        # print(temp)
    return temp

locations = get_location_ranges(seed_ranges)
print(locations)
print(min(locations)[0])
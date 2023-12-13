with open("input.txt", "r") as f:
    lines = f.read()

def first_part():
    seeds = [int(x) for x in lines.split("\n")[0].split()[1::]]
    maps = [[[int(x) for x in map.split()] for map in line.split("\n")[1::]] for line in lines.split("\n\n")[1::]]
    # now THIS ^ is Python
    for i, seed in enumerate(seeds):
        for map in maps:
            for transform in map:
                if seed in range(transform[1], transform[1] + transform[2]):
                    seed += transform[0] - transform[1]
                    break
        seeds[i] = seed
    print(min(seeds))
    
def second_part():
    parsed_seeds = [int(x) for x in lines.split("\n")[0].split()[1::]]
    seeds = []
    for i in range(0, len(parsed_seeds), 2):
        for x in range(parsed_seeds[i], parsed_seeds[i] + parsed_seeds[i + 1]):
            seeds.append(x)
    seeds.sort()
    
    maps = [[[int(x) for x in map.split()] for map in line.split("\n")[1::]] for line in lines.split("\n\n")[1::]]
    for i in range(len(seeds)):
        for map in enumerate(maps):
            for trans in map:
                if trans[1] <= seeds[i] < trans[1] + trans[2]:
                    seeds[i] += trans
                    break
    # not a complete solution - it's terminating because OOM
    print("NOT COMPLETED")

first_part()
second_part()
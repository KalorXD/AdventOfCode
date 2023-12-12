with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def first_part():
    sum = 0
    for line in lines:
        springs, groups = line.split()
        groups = [int(group) for group in groups.split(",")]
        unknown = springs.count("?")
        count, cur_pos = 0, 0
        for i in range(2**unknown):
            temp_springs = springs
            positions = f'{i:0{unknown}b}'
            for position in positions:
                if position == "0":
                    temp_springs = temp_springs.replace("?", ".", 1)
                else:
                    temp_springs = temp_springs.replace("?", "#", 1)
            temp_springs = [len(spring.strip()) for spring in temp_springs.replace(".", " ").split()]
            if temp_springs == groups:
                count += 1
        sum += count
    print(sum)

def second_part():
    # NOT COMPLETED
    print("NOT COMPLETED")

first_part()
second_part()
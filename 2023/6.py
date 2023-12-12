import math

with open("input.txt", "r") as f:
    lines = f.readlines()

def first_part():
    times = lines[0].split()[1::]
    distances = lines[1].split()[1::]   
    sum = 1
    for (time, distance) in zip(times, distances):
        count = 0
        for i in range(int(time) + 1):
            if (int(time) - i) * i > int(distance):
                count += 1
        sum *= count
    print(sum)

def second_part():
    times = [''.join(lines[0].split()[1::])]
    distances = [''.join(lines[1].split()[1::])]
    time = int(times[0])
    distance = int(distances[0])
    count = 0
    for i in range(int(time) + 1):
        if (time - i) * i > distance:
            count += 1
    print(count)
    
first_part()
second_part()
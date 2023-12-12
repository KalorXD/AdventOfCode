import math

with open("2023/input.txt", "r") as f:
    lines = f.readlines()
    
times = [int(x) for x in lines[0].split()[1::]]
distances = [int(x) for x in lines[1].split()[1::]]
sum = 1

time = times[0]
distance = distances[0]
print(time, distance)
count = 0
for i in range(time + 1):
    if (time - i) * i > distance:
        count += 1
print(count)
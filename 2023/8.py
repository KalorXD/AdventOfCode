from math import gcd

with open("2023/input.txt", "r") as f:
    lines = f.readlines()
    
moves = lines[0].strip()
nodes = dict()

for line in lines[2::]:
    nodes[line[:3]] = line[line.find("(") + 1: line.find(")")].split(", ")

cur = [x for x in nodes if x[-1] == "A"]
count = [0 for x in cur]
print(cur)
i = 0
for x in cur:
    while x[-1] != "Z":
        if moves[count[i]%len(moves)] == "L":
            x = nodes[x][0]
        if moves[count[i]%len(moves)] == "R":
            x = nodes[x][1]
        
        count[i] += 1
    print(count[i])
    i += 1

lcm = 1
for i in count:
    lcm = lcm * i // gcd(lcm, i)
    
print(lcm)
with open("2023/input.txt", "r") as f:
    lines = f.readlines()

seeds = [int(x) for x in lines[0].split()[1::]]

inMap = False
for i in range(2, len(lines)):
    if "map" in lines[i]:
        inMap = True
    if lines[i] == "\n":
        inMap = False
    
    
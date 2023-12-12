with open("2022/input.txt", "r") as f:
    lines = f.read()

a = sum(sorted([sum([int(x) for x in line.split("\n")]) for line in lines.split("\n\n")], reverse=True)[:3])
print(a)
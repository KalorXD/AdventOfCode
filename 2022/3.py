chars = " "
for i in range(26):
    chars += chr(ord('a') + i)
for i in range(26):
    chars += chr(ord('A') + i)
    
with open("2022/input.txt", "r") as f:
    lines = f.readlines()
    
sum = 0
for i in range(0, len(lines), 3):
    line_a = set(lines[i].strip())
    line_b = set(lines[i+1].strip())
    line_c = set(lines[i+2].strip())
    letter = list(line_c.intersection(line_a.intersection(line_b)))[0]
    print(line_a, line_b, line_c)
    print(letter)
    sum += chars.find(letter)
print(sum)
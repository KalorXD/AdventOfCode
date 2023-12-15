with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

def first_part():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                pointer_i = i
                pointer_j = j
                while lines[pointer_i - 1][pointer_j] == "." and pointer_i - 1 >= 0 and pointer_j - 1 >= 0:
                    lines[pointer_i - 1][pointer_j] = "O"
                    lines[pointer_i][pointer_j] = "."
                    pointer_i -= 1
    count = 0
    for line in lines:
        print(''.join(line))
    for i, line in enumerate(lines):
        count += line.count("O") * (len(lines) - i)
        print(f"{i}: {line.count('O')}, {len(lines) - i}, {count}")
    print(count)

def second_part():
    # NOT COMPLETED
    print("NOT COMPLETED")

first_part()
second_part()
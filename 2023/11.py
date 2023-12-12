with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

expanded_rows = []
for i in range(len(lines)):
    if len(set(lines[i])) == 1:
        expanded_rows.append(i)

expanded_columns = []
for j in range(len(lines[0])):
    isEmpty = True
    for i in range(len(lines)):
        if lines[i][j] != ".":
            isEmpty = False
    if isEmpty:
        expanded_columns.append(j)

coords = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != ".":
            coords.append((i, j))

def first_part():
    sum = 0
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            for x in range(min(coords[i][0], coords[j][0]), max(coords[i][0], coords[j][0])):
                sum += 1 + 1 * (x in expanded_rows)
            for y in range(min(coords[i][1], coords[j][1]), max(coords[i][1], coords[j][1])):
                sum += 1 + 1 * (y in expanded_columns)

    print(sum)

def second_part():
    sum = 0
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            for x in range(min(coords[i][0], coords[j][0]), max(coords[i][0], coords[j][0])):
                sum += 1 + 999_999 * (x in expanded_rows)
            for y in range(min(coords[i][1], coords[j][1]), max(coords[i][1], coords[j][1])):
                sum += 1 + 999_999 * (y in expanded_columns)

    print(sum)

first_part()
second_part()
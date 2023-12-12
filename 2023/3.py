import re

with open("2023/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

def first_part():
    sum = 0
    for i in range(len(lines)):
        if len(set(re.findall(r'\d+', lines[i]))) != len(re.findall(r'\d+', lines[i])):
            print("uh oh", i)
        cur_pos = 0
        for number in re.findall(r'\d+', lines[i]):
            row, column = i, lines[i].find(number, cur_pos)
            cur_pos = column + len(number)
            isPartNumber = False
            for x in range(row - 1, row + 2):
                for y in range(column - 1, column + len(number) + 1):
                    try:
                        if lines[x][y] not in ".0123456789":
                            isPartNumber = True
                    except:
                        continue
            if isPartNumber:
                sum += int(number)
            
    print(sum)

def second_part():
    # not completed

first_part()
second_part()
with open("2023/input.txt", "r") as f:
    lines = f.read().split("\n")

def goThroughRoute(lines, start_pos):
    cur_pos = start_pos
    direction = 0      
    # 0 - вверх, 1 - вправо, 2 - вниз, 3 - влево
    
    if lines[start_pos[0]][start_pos[1] - 1] in "-FL":
        cur_pos = (start_pos[0], start_pos[1] - 1)
        if lines[start_pos[0]][start_pos[1] - 1] == "-":
            direction = 3
        elif lines[start_pos[0]][start_pos[1] - 1] == "F":
            direction = 2
        else:
            direction = 0
    elif lines[start_pos[0]][start_pos[1] + 1] in "-J7":
        cur_pos = (start_pos[0], start_pos[1] + 1)
        if lines[start_pos[0]][start_pos[1] + 1] == "-":
            direction = 1
        elif lines[start_pos[0]][start_pos[1] + 1] == "J":
            direction = 0
        else:
            direction = 2
    elif lines[start_pos[0] - 1][start_pos[1]] in "|7F":
        cur_pos = (start_pos[0] - 1, start_pos[1])
        if lines[start_pos[0] - 1][start_pos[1]] == "|":
            direction = 0
        elif lines[start_pos[0] - 1][start_pos[1]] == "F":
            direction = 1
        else:
            direction = 3
    elif lines[start_pos[0] + 1][start_pos[1]] in "|JL":
        cur_pos = (start_pos[0] + 1, start_pos[1])
        if lines[start_pos[0] + 1][start_pos[1]] == "|":
            direction = 2
        elif lines[start_pos[0] + 1][start_pos[1]] == "J":
            direction = 3
        else:
            direction = 1
    
    length = 1
    
    while cur_pos != start_pos:
        if direction == 0:
            cur_pos = (cur_pos[0] - 1, cur_pos[1])
            point = lines[cur_pos[0]][cur_pos[1]]
            if point == "|":
                direction = 0
            elif point == "F":
                direction = 1
            elif point == "7":
                direction = 3
        elif direction == 1:
            cur_pos = (cur_pos[0], cur_pos[1] + 1)
            point = lines[cur_pos[0]][cur_pos[1]]
            if point == "-":
                direction = 1
            elif point == "J":
                direction = 0
            elif point == "7":
                direction = 2
        elif direction == 2:
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
            point = lines[cur_pos[0]][cur_pos[1]]
            if point == "|":
                direction = 2
            elif point == "J":
                direction = 3
            elif point == "L":
                direction = 1
        elif direction == 3:
            cur_pos = (cur_pos[0], cur_pos[1] - 1)
            point = lines[cur_pos[0]][cur_pos[1]]
            if point == "-":
                direction = 3
            elif point == "F":
                direction = 2
            elif point == "L":
                direction = 0
        length += 1

    return length

start_pos = (0, 0)
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "S":
            start_pos = (i, j)
            break

length = goThroughRoute(lines, start_pos)
print(length // 2)
with open("input.txt", "r") as f:
    lines = [map.split("\n") for map in f.read().split("\n\n")]
    lines_flipped = [[''.join([line[i] for line in map]) for i in range(len(map[0]))] for map in lines]
    print(lines)
    print(lines_flipped)

def first_part():
    count = 0
    for map in lines_flipped:
        for j in range(len(map) - 1):
            hasMirror = True
            if lines_flipped[j] == lines_flipped[j+1]:
                for pos in range(j - 1, -1, -1):
                    try:
                        if lines_flipped[pos] != lines_flipped[j + j - pos + 1]:
                            hasMirror = False
                    except:
                        break
            if hasMirror:
                count += j
                break
    
    for map in lines:
        hasMirror = False
        for j in range(len(map) - 1):
            if lines[j] == lines[j+1]:
                for pos in range(j - 1, -1, -1):
                    try:
                        if lines[pos] != lines[j + j - pos + 1]:
                            hasMirror = False
                    except:
                        break
            if hasMirror:
                count += j * 100
                break
    # NOT COMPLETED
    print("NOT COMPLETED")

def second_part():
    # NOT COMPLETED
    print("NOT COMPLETED")

first_part()
second_part()
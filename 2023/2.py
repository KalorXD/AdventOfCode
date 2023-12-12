colors = {
            "red": 12, 
            "green":13, 
            "blue":14
        }

with open("2023/input.txt", "r") as new_file:
    lines = new_file.readlines()

sum = 0
for line in lines:
    isPossible = True
    start_point = line.find(":")
    id = int(line[5:start_point])
    game = line[start_point + 2::].strip().split("; ")
    color_counter = {"red": 0, "blue": 0, "green": 0}
    for move in game:
        move = move.split(", ")
        move_colors = {"red": 0, "blue": 0, "green": 0}
        for element in move:
            element = element.split()
            element[0] = int(element[0])
            move_colors[element[1]] += element[0]
        for key in move_colors:
            color_counter[key] = max(color_counter[key], move_colors[key])
    sum += color_counter["blue"] * color_counter["red"] * color_counter["green"]

print(sum)
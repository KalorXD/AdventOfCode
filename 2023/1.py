import re

spelt_numbers = "one two three four five six seven eight nine 1 2 3 4 5 6 7 8 9".split()

with open("input.txt", "r") as new_file:
    lines = new_file.readlines()

def first_part():
    sum = 0
    for line in lines:
        cur_numbers = re.findall(r'\d', line)
        sum += int(cur_numbers[0] + cur_numbers[-1])
    print(sum)

def second_part():
    sum = 0
    for line in lines:
        cur_numbers = ['0', '0']
        for i in range(0, len(line)):
            cur_position = [len(line), 0]
            for number in spelt_numbers:
                if line.find(number) < cur_position[0] and line.find(number) != -1:
                    cur_position = [line.find(number), len(number)]
            cur_numbers[0] = line[cur_position[0]:cur_position[0]+cur_position[1]]
        for i in range(len(line) - 1, -1, -1):
            cur_position = [-1, 0]
            for number in spelt_numbers:
                if line.rfind(number) > cur_position[0] and line.rfind(number) != -1:
                    cur_position = [line.rfind(number), len(number)]
            cur_numbers[1] = line[cur_position[0]:cur_position[0]+cur_position[1]]
        for i in range(2):
            if not cur_numbers[i].isnumeric():
                cur_numbers[i] = str(spelt_numbers.index(cur_numbers[i]) + 1)
        sum += int(cur_numbers[0] + cur_numbers[1])
    print(sum)

first_part()
second_part()
def generateFirstElem(array):
    if array == [0] * len(array):
        array = [0] + array
    else:
        diff = generateFirstElem([array[i+1] - array[i] for i in range(len(array) - 1)])
        array = [array[0] - diff[0]] + array
    return array

def generateNextElem(array):
    if array == [0] * len(array):
        array = array + [0]
    else:
        diff = generateNextElem([array[i+1] - array[i] for i in range(len(array) - 1)])
        array = array + [array[-1] + diff[-1]]
    return array

with open("input.txt", "r") as f:
    lines = f.readlines()

def first_part():
    sum = 0
    for line in lines:
        array = generateNextElem([int(x) for x in line.split()])
        sum += array[-1]
    print(sum)

def second_part():
    sum = 0
    for line in lines:
        array = generateFirstElem([int(x) for x in line.split()])
        sum += array[0]
    print(sum)
    
first_part()
second_part()
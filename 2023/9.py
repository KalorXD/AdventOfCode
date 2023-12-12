def generateNextElem(array):
    if array == [0] * len(array):
        array = [0] + array
    else:
        diff = generateNextElem([array[i+1] - array[i] for i in range(len(array) - 1)])
        array = [array[0] - diff[0]] + array
    return array
        

with open("2023/input.txt", "r") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    array = generateNextElem([int(x) for x in line.split()])
    print(array)
    sum += array[0]

print(sum)
with open("input.txt", "r") as f:
    line = f.readline().strip().split(",")

def calculateHash(word):
    hash = 0
    for letter in word:
        hash += ord(letter)
        hash *= 17
        hash %= 256
    return hash

def first_part():
    result = sum([calculateHash(word) for word in line])
    print(result)

def second_part():
    # NOT COMPLETED
    print("NOT COMPLETED")

first_part()
second_part()
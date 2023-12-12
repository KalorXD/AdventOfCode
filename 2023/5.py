with open("input.txt", "r") as f:
    lines = f.readlines()

def first_part():
    seeds = [int(x) for x in lines[0].split()[1::]]

    inMap = False
    for i in range(2, len(lines)):
        if "map" in lines[i]:
            inMap = True
        if lines[i] == "\n":
            inMap = False
    # INCOMPLETE
    print("NOT COMPLETED")
    
def second_part():
    # NOT COMPLETED
    print("NOT COMPLETED")
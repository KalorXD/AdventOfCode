from collections import defaultdict

with open("2023/input.txt", "r") as f:
    lines = f.readlines()

i = 0
types = defaultdict(int)
while i < len(lines):
    id = int(lines[i][4:lines[i].find(":")])
    types[i] += 1
    cards = lines[i][lines[i].find(":") + 2::].strip().split("|")
    win_cards = cards[0].split()
    player_cards = cards[1].split()
    count = len(set(win_cards) & set(player_cards))
    for j in range(count):
        types[i + 1 + j] += types[i]
    i += 1

print(sum(types.values()))
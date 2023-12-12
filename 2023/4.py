from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

types = defaultdict(int)
summ = 0
for i in range(len(lines)):
    id = int(lines[i][4:lines[i].find(":")])
    types[i] += 1
    cards = lines[i][lines[i].find(":") + 2::].strip().split("|")
    win_cards = cards[0].split()
    player_cards = cards[1].split()
    count = len(set(win_cards) & set(player_cards))
    for j in range(count):
        types[i + 1 + j] += types[i]
    if count > 0:
        summ += 2 ** (count - 1)

print(summ)
print(sum(types.values()))
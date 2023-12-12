from collections import Counter

cards_letters = "J23456789TQKA"

def translateCardsToNumbers(cards):
    number = ''
    for x in cards:
        number += hex(cards_letters.find(x))[2::]
    return number
        
def giveTypeStrength(cards):
    if "J" in cards and cards != "JJJJJ":
        #print(f"before: {cards} ",end="")
        count = Counter(cards)
        del count["J"]
        cards = cards.replace("J", count.most_common(1)[0][0])
        #print(f"after: {cards}")
    count = Counter(cards)
    if len(count) == 1:
        return 7
    elif len(count) == 2:
        if count.most_common(1)[0][1] == 4:
            return 6
        else:
            return 5
    elif len(count) == 3:
        if count.most_common(1)[0][1] == 3:
            return 4
        if count.most_common(2)[0][1] == count.most_common(2)[1][1] == 2:
            return 3
    elif len(count) == 4:
        return 2
    elif len(count) == 5:
        if "J" in cards:
            print(cards)
        return 1

with open("2023/input.txt", "r") as f:
    lines = f.readlines()
    
players = [{"cards": line.strip().split()[0], "bet": int(line.strip().split()[1]), "type_strength": giveTypeStrength(line.strip().split()[0])} for line in lines]
players = sorted(players, key=lambda x: x["type_strength"])

passed_length = 0
for i in range(1, 7 + 1):
    players_sort = sorted([x for x in players if x["type_strength"] == i], key=lambda x: int(translateCardsToNumbers(x["cards"]), 13))
    for j in range(passed_length, passed_length + len(players_sort)):
        players[j] = players_sort[j - passed_length]
    passed_length += len(players_sort)

#for player in players:
    #if "J" in player["cards"]: 
        #print(player, int(translateCardsToNumbers(player["cards"]), 13))

sum = 0
for i in range(len(players)):
    sum += (i + 1) * players[i]["bet"]
    
print(sum)
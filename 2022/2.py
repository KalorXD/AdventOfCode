player = "XYZ"      # X - rock, Y - paper, Z - scissors
opponent = "ABC"    # A - rock, B - paper, C - scissors

# wins = ["C X", "A Y", "B Z"]
# loses = ["B X", "C Y", "A Z"]
# win for player:   C X, A Y, B Z
# tie for both:     A X, B Y, C Z
# win for opponent: B X, C Y, A Z

with open("2022/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
score = 0
for line in lines:
    o, p = line[0], line[2]
    score += player.find(p) * 3 + 1

print(score)
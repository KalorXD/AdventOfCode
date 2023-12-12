import re

length = len("48.................501....33.....622..............763.........331.................161.683......................................980..........")

with open("2023/input.txt", "r") as f:
    lines = ''.join([line.strip() for line in f.readlines()])

a = re.findall(r'\d+', lines)

# INCOMPLETE
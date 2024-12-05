import re

with open('./input.txt') as file:
    lines = file.read()

pattern = r"mul\((?:[1-9][0-9]{0,2}|0),(?:[1-9][0-9]{0,2}|0)\)|do\(\)|don't\(\)"
total_sum = 0
keep = True
matches = re.findall(pattern, lines)
for match in matches:
    if match == "do()":
        keep = True
    elif match == "don't()":
        keep = False
    else:
        if keep:
            x, y = map(int, match[4:-1].split(","))
            total_sum += x*y
print(total_sum)
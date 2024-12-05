import re

with open('./input.txt') as file:
    lines = file.readlines()

pattern = r"mul\(([1-9][0-9]{0,2}|0),([1-9][0-9]{0,2}|0)\)"
matches = [re.findall(pattern, line) for line in lines]

# Flatten the list of matches
matches = [match for sublist in matches for match in sublist]

# Multiply the two entries in each tuple and progressively sum each result
total_sum = 0
for match in matches:
    total_sum += int(match[0]) * int(match[1])

print(total_sum)

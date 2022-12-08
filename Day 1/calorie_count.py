import os

calorie_lines = []
with open("input.txt") as calorie_file:
    calorie_lines = calorie_file.readlines()

calorie_counts = []

current_count = 0
for line in calorie_lines:
    if line == '\n':
        calorie_counts.append(current_count)
        current_count = 0
    elif calories := int(line):
        current_count += calories

calorie_counts.sort()

# Puzzle 1 solution
print(calorie_counts[-1])

# Puzzle 2 solution
print(sum(calorie_counts[-3:]))
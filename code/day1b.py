#!/usr/bin/env python3

col_1 = []
col_2 = []

with open("../data/day1a.txt", "r") as f:
    for line in f:
        col_1.append(int(line.split("   ")[0]))
        col_2.append(int(line.split("   ")[1]))

counter = 0

for num in col_1:
    counter = counter + ((num) * (col_2.count(num)))

print(counter)
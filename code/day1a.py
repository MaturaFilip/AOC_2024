#!/usr/bin/env python3

col_1 = []
col_2 = []

with open("../data/day1a.txt", "r") as f:
    for line in f:
        col_1.append(line.split("   ")[0])
        col_2.append(line.split("   ")[1])

col_1.sort()
col_2.sort()

dif = list(map(lambda x, y: abs(int(x)-int(y)), col_1, col_2))

counter = sum(dif)

print(counter)


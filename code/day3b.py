#!/usr/bin/env python3
import re

switcher = True

counter = 0
with open("../data/day3.txt", "r") as f:
    content = f.read()

for i in re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", content):
    if i == "do()":
        switcher = True
    if i == "don't()":
        switcher = False
    if switcher == True and i != "do()":
        x = re.findall("\d{1,3}", i)
        counter += int(x[0]) * int(x[1])
    #print(i)
print(counter)
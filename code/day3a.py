#!/usr/bin/env python3
import re

counter = 0
with open("../data/day3.txt", "r") as f:
    content = f.read()

for i in re.findall("mul\(\d{1,3},\d{1,3}\)", content):
    x = re.findall("\d{1,3}", i)
    counter += int(x[0]) * int(x[1])

print(counter)
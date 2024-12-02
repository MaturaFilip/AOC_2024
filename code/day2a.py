#!/usr/bin/env python3

counter = 0

with open("../data/day2.txt", "r") as f:
    for line in f:
        x = line.split()
        row = [int(item) for item in x]
        
        min_so_far = float("inf")
        max_so_far = float("-inf")
        increasing = False
        decreasing = False

        # find increasing
        for index, num in enumerate(row):
            if index == 0:
                max_so_far = num
                continue
            if num == (max_so_far)+1 or num == (max_so_far)+2 or num == (max_so_far)+3: 
                max_so_far = num
                increasing = True
            else:
                increasing = False
                break

        if increasing == True:
            counter += 1

        # find decreasing
        for index, num in enumerate(row):
            if index == 0:
                min_so_far = num
                continue
            if num == (min_so_far)-1 or num == (min_so_far)-2 or num == (min_so_far)-3: 
                min_so_far = num
                decreasing = True
            else:
                decreasing = False
                break

        if decreasing == True:
            counter += 1


print(counter)

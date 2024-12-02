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
        true_list_inc = []
        true_list_dec = []

        # find increasing
        for i, item in enumerate(row):
            row.pop(i)
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
                true_list_dec.append(True)
            row.insert(i,item)

        if True in true_list_inc:
            counter +=1

        for i, item in enumerate(row):
            row.pop(i)
            for index, num in enumerate(row):
                if index == 0:
                    max_so_far = num
                    continue
                if num == (max_so_far)-1 or num == (max_so_far)-2 or num == (max_so_far)-3: 
                    max_so_far = num
                    increasing = True
                else:
                    increasing = False
                    break

            if increasing == True:
                true_list_dec.append(True)
            row.insert(i,item)

        if True in true_list_dec:
            counter +=1
print(counter)
import numpy as np

with open("input2.txt") as file:
    ids = file.readlines()
    twos = 0
    threes = 0
    for id in ids:
        two = False
        three = False
        for i in id:
            if id.count(i) == 2:
                two = True
            elif id.count(i) == 3:
                three = True
        if two:
            twos += 1
        if three:
            threes += 1
    print(twos*threes)

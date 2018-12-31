import numpy as np

with open("input2.txt") as file:
    ids = file.readlines()
    past = []
    for id in ids:
        for p in past:
            mismatch = 0
            for i in range(len(id)):
                if id[i] != p[i]:
                  mismatch += 1
                if mismatch > 1:
                    break
            if mismatch == 1:
                print("id1: " + id)
                print("id2: " + p)
        past = np.append(past, id)

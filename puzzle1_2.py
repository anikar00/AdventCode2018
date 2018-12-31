import numpy as np

with open("input1.txt") as file:
    vals = file.readlines()
    total = 0
    frequencies = []
    notdone = True
    while notdone:
        for x in vals:
            total += int(x)
            if total in frequencies:
                print(total)
                notdone = False
                break
            else:
                frequencies = np.append(frequencies, total)

import numpy as np

with open("input3.txt") as file:
    options = file.readlines()
    fabric = np.full((1000, 1000), 0)
    count = 1
    for cut in options:
        at = cut.find('@')
        comma = cut.find(',')
        colon = cut.find(':')
        cross = cut.find('x')

        left = int(cut[at + 2: comma])
        down = int(cut[comma + 1: colon])
        width = int(cut[colon + 2: cross])
        height = int(cut[cross + 1:])

        for w in range(width):
            for l in range(height):
                fabric[left + w, down + l] += 1

    print((fabric > 1).sum())

import numpy as np

with open("input3.txt") as file:
    options = file.readlines()
    fabric = np.full((1000, 1000), 0)
    count = 1
    possibles = []

    for cut in options:
        at = cut.find('@')
        comma = cut.find(',')
        colon = cut.find(':')
        cross = cut.find('x')

        id = int(cut[1:at - 1])
        left = int(cut[at + 2: comma])
        down = int(cut[comma + 1: colon])
        width = int(cut[colon + 2: cross])
        height = int(cut[cross + 1:])


        overlaps = False
        for w in range(width):
            for l in range(height):
                if fabric[left + w, down + l] > 0:
                    overlaps = True
                fabric[left + w, down + l] += 1

        if overlaps == False:
            possibles = np.append(possibles, id)

    try_at = len(possibles) - 1
    solution = False
    while solution == False :
        id = int(possibles[try_at])
        cut = options[id - 1]

        at = cut.find('@')
        comma = cut.find(',')
        colon = cut.find(':')
        cross = cut.find('x')
        left = int(cut[at + 2: comma])
        down = int(cut[comma + 1: colon])
        width = int(cut[colon + 2: cross])
        height = int(cut[cross + 1:])

        works = True
        for w in range(width):
            for l in range(height):
                if fabric[left + w, down + l] != 1:
                    works = False
                    break
            if works == False:
                break

        if works == True:
            print(id)
            solution = True

        try_at = try_at - 1

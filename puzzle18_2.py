with open("input18.txt") as file:
    land = [[a for a in line.strip()] for line in file.readlines()]

def classify(spot):
    global land
    global open_surround
    global tree_surround
    global lumber_surround
    if land[spot[0]][spot[1]] == '.':
        open_surround += 1
    elif land[spot[0]][spot[1]] == '|':
        tree_surround += 1
    elif land[spot[0]][spot[1]] == '#':
        lumber_surround += 1

lumber_counts = []
for min in range(1700):
    new_land = [['' for i in range(len(land))] for j in range(len(land[0]))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            open_surround = 0
            tree_surround = 0
            lumber_surround = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0: continue
                    if 0 <= i+di < len(land) and 0 <= j+dj < len(land[0]):
                        classify((i+di, j+dj))
            if land[i][j] == '.' and tree_surround >= 3:
                new_land[i][j] = '|'
            elif land[i][j] == '|' and lumber_surround >= 3:
                new_land[i][j] = '#'
            elif land[i][j] == '#' and (lumber_surround == 0 or tree_surround == 0):
                new_land[i][j] = '.'
            else:
                new_land[i][j] = land[i][j]
    land = new_land

    lumber = 0
    wood = 0
    for line in land:
        for l in line:
            if l == '#':
                lumber += 1
            elif l == '|':
                wood += 1
    if (min+1) % 100 == 0:
        print(lumber * wood)

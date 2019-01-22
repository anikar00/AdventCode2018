class Space:
    def __init__(self, type):
        self.type = type
        self.hp = -10
        if type == 'G' or type == 'E':
            self.hp = 200

def enemy(unit):
    enemy = ''
    if unit.type == 'E':
        enemy = 'G'
    elif unit.type == 'G':
        enemy = 'E'
    return enemy

def nextdoor_enemy(unit):
    global board
    pos_r = unit[0]
    pos_c = unit[1]
    enemy_type = enemy(unit[2])

    enemies = []
    if board[pos_r-1][pos_c].type == enemy_type:
        enemies.append([pos_r-1, pos_c])
    if board[pos_r][pos_c-1].type == enemy_type:
        enemies.append([pos_r, pos_c-1])
    if board[pos_r][pos_c+1].type == enemy_type:
        enemies.append([pos_r, pos_c+1])
    if board[pos_r+1][pos_c].type == enemy_type:
        enemies.append([pos_r+1, pos_c])
    enemy_pos = None
    if(len(enemies) == 1):
        enemy_pos = enemies[0]
    elif(len(enemies) > 1):
        enemy_pos = enemies[0]
        min_hp = board[enemy_pos[0]][enemy_pos[1]].hp
        for pos in enemies:
            if board[pos[0]][pos[1]].hp < min_hp:
                enemy_pos = pos
                min_hp = board[pos[0]][pos[1]].hp

    return enemy_pos

def nearest_enemy(unit):
    global board
    pos_r = unit[0]
    pos_c = unit[1]

    pinged = []
    to_ping = [[pos_r, pos_c]]
    enemies = []
    dist = 0
    while len(to_ping) > 0:
        dist += 1
        next_ping = []
        for p in to_ping:
            if p in pinged:
                continue
            else:
                pinged.append(p)
                enemy_type = enemy(unit[2])
                if p[0] + 1 < len(board) and board[p[0] + 1][p[1]].type == enemy_type:
                    enemies.append(p)
                elif p[0] > 0 and board[p[0] - 1][p[1]].type == enemy_type:
                    enemies.append(p)
                elif p[1] + 1 < len(board[0]) and board[p[0]][p[1] + 1].type == enemy_type:
                    enemies.append(p)
                elif p[1] > 0 and board[p[0]][p[1] - 1].type == enemy_type:
                    enemies.append(p)
                else:
                    if p[0] + 1 < len(board) and board[p[0] + 1][p[1]].type == '.':
                        next_ping.append([p[0] + 1, p[1]])
                    if p[0] > 0 and board[p[0] - 1][p[1]].type == '.':
                        next_ping.append([p[0] - 1, p[1]])
                    if p[1] + 1 < len(board[0]) and board[p[0]][p[1] + 1].type == '.':
                        next_ping.append([p[0], p[1] + 1])
                    if p[1] > 0 and board[p[0]][p[1] - 1].type == '.':
                        next_ping.append([p[0], p[1] - 1])

        if len(enemies) > 0:
            return [sorted(enemies)[0], dist]
        to_ping = next_ping
    return [None, 0]

not_complete = True
power = 4
while not_complete == True:
    with open("input15.txt") as file: board = [[Space(spot) for spot in line.strip()] for line in file.readlines()]
    num_goblins = num_elves = 0
    units = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].type == "G":
                num_goblins += 1
                units.append([i, j, board[i][j]])
            elif board[i][j].type == "E":
                num_elves += 1
                units.append([i, j, board[i][j]])

    round = 0
    rem_one = False
    quit = False
    while num_goblins > 0 and quit == False:
        units.sort(key = lambda unit: (unit[0], unit[1]))

        to_remove = []
        for unit in units:
            if unit in to_remove:
                continue

            enemy_loc = nextdoor_enemy(unit)
            if enemy_loc == None:
                [enemy_loc, d] = nearest_enemy(unit)
                if enemy_loc == None:
                    continue
                else:
                    if nearest_enemy([unit[0]-1, unit[1], unit[2]]) == [enemy_loc, d-1] and board[unit[0]-1][unit[1]].type == '.':
                        board[unit[0]-1][unit[1]] = unit[2]
                        board[unit[0]][unit[1]] = Space('.')
                        unit[0] -= 1
                    elif nearest_enemy([unit[0], unit[1]-1, unit[2]]) == [enemy_loc, d-1] and board[unit[0]][unit[1]-1].type == '.':
                        board[unit[0]][unit[1]-1] = unit[2]
                        board[unit[0]][unit[1]] = Space('.')
                        unit[1] -= 1
                    elif nearest_enemy([unit[0], unit[1]+1, unit[2]]) == [enemy_loc, d-1] and board[unit[0]][unit[1]+1].type == '.':
                        board[unit[0]][unit[1]+1] = unit[2]
                        board[unit[0]][unit[1]] = Space('.')
                        unit[1] += 1
                    elif nearest_enemy([unit[0]+1, unit[1], unit[2]]) == [enemy_loc, d-1] and board[unit[0]+1][unit[1]].type == '.':
                        board[unit[0]+1][unit[1]] = unit[2]
                        board[unit[0]][unit[1]] = Space('.')
                        unit[0] += 1

                    enemy_loc = nextdoor_enemy(unit)

            if enemy_loc != None:
                if board[enemy_loc[0]][enemy_loc[1]].type == 'E':
                    board[enemy_loc[0]][enemy_loc[1]].hp -= 3
                    if board[enemy_loc[0]][enemy_loc[1]].hp <= 0:
                        quit = True
                        power += 1
                else:
                    board[enemy_loc[0]][enemy_loc[1]].hp -= power
                    if board[enemy_loc[0]][enemy_loc[1]].hp <= 0:
                        num_goblins -= 1
                        if num_goblins == 0:
                            rem_one = True
                        board[enemy_loc[0]][enemy_loc[1]] = Space('.')
                        for u in units:
                            if u[0] == enemy_loc[0] and u[1] == enemy_loc[1]:
                                to_remove.append(u)
        for r in to_remove:
            units.remove(r)

        if rem_one == False:
            round += 1
    if num_goblins == 0:
        not_complete = False

        hit_total = 0
        for unit in units:
            hit_total += unit[2].hp
        print(round*hit_total)

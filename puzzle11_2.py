import numpy as np

SERIAL_NUMBER = 3214 # input
GRID_SIZE = 300

power_levels = np.full((GRID_SIZE, GRID_SIZE), 0) # at (i, j) we store power level of cell at y = i+1, x = j+1

# Computing power of each cell
for x in range(1, GRID_SIZE + 1):
    for y in range(1, GRID_SIZE + 1):
        rack_ID = (x + 10)
        power = (rack_ID * y + SERIAL_NUMBER) * rack_ID
        if str(power)[-3]:
            power = int(str(power)[-3]) - 5
        else:
            power = -5
        power_levels[y-1, x-1] = power

current_max = 0
current_index = [0, 0, 0]

for size in range(1, GRID_SIZE + 1):
    group_levels = np.asarray([[ power_levels[i:(i+size), j:(j+size)].sum() for i in range(GRID_SIZE - 2)]
        for j in range(GRID_SIZE - 2)]) # summing up three by threes and reinverting to be in x, y order
    max_index = np.unravel_index(group_levels.argmax(), group_levels.shape) # finding index of maximum 3 by 3 power
    if current_max < group_levels[max_index]:
        current_max = group_levels[max_index]
        current_index = [max_index[0] + 1, max_index[1] + 1, size]
        print(current_index)

print("X: " + str(current_index[0]))
print("Y: " + str(current_index[1]))
print("size: " + str(current_index[2]))

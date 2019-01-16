import numpy as np

SERIAL_NUMBER = 3214 # input

power_levels = np.full((300, 300), 0) # at (i, j) we store power level of cell at y = i+1, x = j+1

# Computing power of each cell
for x in range(1, 301):
    for y in range(1, 301):
        rack_ID = (x + 10)
        power = (rack_ID * y + SERIAL_NUMBER) * rack_ID
        if str(power)[-3]:
            power = int(str(power)[-3]) - 5
        else:
            power = -5
        power_levels[y-1, x-1] = power

group_level = [[ power_levels[i:(i+3), j:(j+3)].sum() for i in range(298)] for j in range(298)] # summing up three by threes and reinverting to be in x, y order
group_level = np.asarray(group_level)

max_index = np.unravel_index(group_level.argmax(), group_level.shape) # finding index of maximum 3 by 3 power

print("X: " + str(max_index[0] + 1))
print("Y: " + str(max_index[1] + 1))

import matplotlib.pyplot as plt
import numpy as np

with open("input10.txt") as file:
    data = file.readlines()

x = np.array([])
y = np.array([])
V_x = np.array([])
V_y = np.array([])

for line in data:
    line_pos = line[:line.find(">") + 1]
    line_vel = line[line.find(">") + 2 :]
    x = np.append(x, int(line_pos[line_pos.find("<") + 1:line_pos.find(",")]))
    y = np.append(y, int(line_pos[line_pos.find(",") + 1: line_pos.find(">")]))
    V_x = np.append(V_x, int(line_vel[line_vel.find("<") + 1:line_vel.find(",")]))
    V_y = np.append(V_y, int(line_vel[line_vel.find(",") + 1: line_vel.find(">")]))

plt.ion()
startTime = 10900
tryFor = 6

thisX = x + V_x * startTime
thisY = -1 * (y + V_y * startTime)
scat = plt.scatter(thisX, thisY)
plt.draw()

for time in range(tryFor):
    t = time + startTime
    thisX = x + V_x * t
    thisY = -1 * (y + V_y * t)
    scat.set_offsets(np.c_[thisX, thisY])
    plt.autoscale()
    plt.pause(0.9)

print("Time: " + str(startTime + tryFor - 1))
plt.waitforbuttonpress()

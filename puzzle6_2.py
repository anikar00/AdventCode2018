with open("input6.txt") as file:
    input = file.readlines()
    points = []
    for line in input:
      point = (int(line[ :line.find(',')]), int(line[line.find(',') + 1:]))
      points.append(point)

def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) # return manhattan distance

x_max = max(pt[0] for pt in points)
x_min = min(pt[0] for pt in points)
y_max = max(pt[1] for pt in points)
y_min = min(pt[1] for pt in points)

x_min_bord = x_min - (x_max - x_min)
x_max_bord = x_max + (x_max - x_min)
y_min_bord = y_min - (y_max - y_min)
y_max_bord = y_max + (y_max - y_min)

inRange = []
for x in range(x_min_bord, x_max_bord):
    for y in range(y_min_bord, y_max_bord):
        total = 0
        for pt in points:
            total += manhattan_dist(pt, (x, y))
        if total < 10000:
            inRange.append((x,y))

print("The area in range is: " + str(len(inRange)))

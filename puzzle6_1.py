with open("input6.txt") as file:
    input = file.readlines()
    points = []
    for line in input:
      point = (int(line[ :line.find(',')]), int(line[line.find(',') + 1:]))
      points.append(point)

def manhattan_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) # return manhattan distance

def closest_points(pt):
    dists = map(lambda p: (manhattan_dist(pt, p), p), points) # save distances as tuples with point
    dists = sorted(dists, key = lambda p: p[0]) # sort based on distances

    closest = []
    count = 0
    while dists[count][0] == dists[0][0]:
        closest.append(dists[count][1])
        count += 1

    return closest

areas = {}
infinite = {}

for point in points:
    areas[point] = 0
    infinite[point] = False

x_max = max(pt[0] for pt in points)
x_min = min(pt[0] for pt in points)
y_max = max(pt[1] for pt in points)
y_min = min(pt[1] for pt in points)

x_min_bord = x_min - (x_max - x_min)
x_max_bord = x_max + (x_max - x_min)
y_min_bord = y_min - (y_max - y_min)
y_max_bord = y_max + (y_max - y_min)

for x in range(x_min_bord, x_max_bord ):
    for pt in closest_points((x, y_min_bord)):
        infinite[pt] = True
    for pt in closest_points((x, y_max_bord)):
        infinite[pt] = True
for y in range(y_min_bord, y_max_bord ):
    for pt in closest_points((x_min_bord, y)):
        infinite[pt] = True
    for pt in closest_points((x_max_bord, y)):
        infinite[pt] = True

for x in range(x_min, x_max):
    for y in range(y_min, y_max):
        closest_pts = closest_points((x, y))
        if len(closest_pts) == 1:
            if infinite[closest_pts[0]] == False:
                areas[closest_pts[0]] += 1

best_area = max(areas.values())
print("The largest area is: " + str(best_area))

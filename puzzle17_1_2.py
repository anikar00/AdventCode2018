import sys
sys.setrecursionlimit(4220)

has_clay = set()
with open("input17.txt") as file:
    claylines = file.readlines()
    for line in claylines:
        line = line.strip()
        spot, ranges = line.split(',')
        spot_val = int(spot[spot.find('=') + 1:])
        range_st = int(ranges[ranges.find('=') + 1:ranges.find('..')])
        range_end = int(ranges[ranges.find('..')+2:])
        if spot[0] == 'x':
            for y in range(range_st, range_end+1):
                has_clay.add((spot_val, y))
        else:
            for x in range(range_st, range_end+1):
                has_clay.add((x, spot_val))

y_min = min(has_clay, key = lambda t: t[1])[1]
y_max = max(has_clay, key = lambda t: t[1])[1]

settled = set()
flows_to = set()

def flow_from(pt):
    below_pt = (pt[0], pt[1] + 1)
    if (below_pt not in has_clay) and (below_pt not in flows_to) and (1 <= below_pt[1] <= y_max):
        flows_to.add(below_pt)
        flow_from(below_pt)
    elif (below_pt in has_clay) or (below_pt in settled):
        left_pt = (pt[0]-1, pt[1])
        right_pt = (pt[0]+1, pt[1])
        overflow = False
        while left_pt not in has_clay:
            if (left_pt[0], left_pt[1] + 1) in has_clay or (left_pt[0], left_pt[1] + 1) in settled:
                left_pt = (left_pt[0]-1, left_pt[1])
            else:
                overflow = True
                break
        while right_pt not in has_clay:
            if (right_pt[0], right_pt[1] + 1) in has_clay or (right_pt[0], right_pt[1] + 1) in settled:
                right_pt = (right_pt[0]+1, right_pt[1])
            else:
                overflow = True
                break
        if overflow == True:
            for i in range(left_pt[0]+1, right_pt[0]):
                flows_to.add((i, pt[1]))
            if (left_pt[0], left_pt[1] + 1) not in has_clay and (left_pt[0], left_pt[1] + 1) not in settled:
                flows_to.add(left_pt)
                flow_from(left_pt)
            if (right_pt[0], right_pt[1] + 1) not in has_clay and (right_pt[0], right_pt[1] + 1) not in settled:
                flows_to.add(right_pt)
                flow_from(right_pt)
        else:
            for i in range(left_pt[0]+1, right_pt[0]):
                settled.add((i, pt[1]))
            flow_from((pt[0], pt[1] - 1))


flow_from((500, 0))

print("Part 1: " + str(len([pt for pt in flows_to | settled if y_min <= pt[1] <= y_max])))
print("Part 2: " + str(len([pt for pt in settled if y_min <= pt[1] <= y_max])))


with open("input1.txt") as file:
    vals = file.readlines()
    total = 0
    for x in vals:
        total += int(x)
    print(total)

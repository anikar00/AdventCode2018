with open("input13.txt") as file:
    lines = [line.rstrip() for line in file.readlines()]

cart_directions = {"<": [1, -1], "^": [0, -1], ">": [1, 1], "v": [0, 1]}
left_order = {"<": "v", "^": "<", ">": "^", "v": ">"}
right_order = {">": "v", "v": "<", "<": "^", "^": ">"}

carts_info = []
for row in range(len(lines)):
    for col in range(len(lines[row])):
        if lines[row][col] in cart_directions.keys():
            carts_info.append([row, col, lines[row][col], 0])

noCrash = True

while noCrash == True:
    carts_info.sort(key = lambda cart: (cart[0], cart[1]))

    for cart in carts_info:
        movement = cart_directions[cart[2]]
        cart[movement[0]] += movement[1]

        if lines[cart[0]][cart[1]] == "\\":
            if cart[2] == ">" or cart[2] == "<":
                cart[2] = right_order[cart[2]]
            else:
                cart[2] = left_order[cart[2]]
        elif lines[cart[0]][cart[1]] == "/":
            if cart[2] == ">" or cart[2] == "<":
                cart[2] = left_order[cart[2]]
            else:
                cart[2] = right_order[cart[2]]
        elif lines[cart[0]][cart[1]] == "+":
            cart[3] += 1
            if cart[3] % 3 == 1:
                cart[2] = left_order[cart[2]]
            elif cart[3] % 3 == 0:
                cart[2] = right_order[cart[2]]

    for cart1 in range(len(carts_info)):
        for cart2 in range(cart1 + 1, len(carts_info)):
            if carts_info[cart1][0] == carts_info[cart2][0] and carts_info[cart1][1] == carts_info[cart2][1]:
                print(str(carts_info[cart1][1]) + ", " + str(carts_info[cart1][0]))
                noCrash = False

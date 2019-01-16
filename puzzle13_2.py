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

while len(carts_info) > 0:
    carts_info.sort(key = lambda cart: (cart[0], cart[1]))

    to_remove = []
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
        for other in range(len(carts_info)):
            if (cart in carts_info) and (carts_info.index(cart) != other):
                if cart[0] == carts_info[other][0] and cart[1] == carts_info[other][1]:
                    to_remove.append(carts_info[other])
                    to_remove.append(cart)

    for cart in to_remove:
        carts_info.remove(cart)

    if len(carts_info) == 1:
        print(str(carts_info[0][1]) + ", " + str(carts_info[0][0]))
        break

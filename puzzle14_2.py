BEFORE_VALS = [7, 9, 3, 0, 6, 1]
VAL_LEN = 6

recipes = [3, 7]
elf1 = 0
elf2 = 1
while (recipes[-VAL_LEN:] != BEFORE_VALS) and (recipes[-(VAL_LEN + 1):-1] != BEFORE_VALS):
    sum = recipes[elf1] + recipes[elf2]
    if len(str(sum)) == 1:
        recipes.append(sum)
    else:
        recipes.append(int(str(sum)[0]))
        recipes.append(int(str(sum)[1]))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

if recipes[-VAL_LEN:] == BEFORE_VALS:
    print(len(recipes) - VAL_LEN)
else:
    print(len(recipes) - VAL_LEN - 1)

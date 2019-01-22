NUM_AFTER = 793061

recipes = [3, 7]
elf1 = 0
elf2 = 1
while len(recipes) < (10 + NUM_AFTER):
    sum = recipes[elf1] + recipes[elf2]
    if len(str(sum)) == 1:
        recipes.append(sum)
    else:
        recipes.append(int(str(sum)[0]))
        recipes.append(int(str(sum)[1]))
    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

print(recipes[NUM_AFTER:(NUM_AFTER+10)])

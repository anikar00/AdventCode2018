def collapse(string):
    notdone = True
    spot = 0
    char1 = string[spot]
    while notdone:
        char2 = string[spot + 1]
        if char1.lower() == char2.lower() and char1 != char2:
            string = string[:spot] + string[spot + 2:]
            if spot > 0:
                spot = spot - 1
        else:
            spot += 1

        if spot + 1 >= len(string):
            notdone = False

        char1 = string[spot]
    return len(string)

with open("input5.txt") as file:
    str = file.readlines()[0].strip()

    min_val = len(str) + 100
    for let in map(chr, range(97, 123)):
        str_test = str.replace(let, "")
        str_test = str_test.replace(let.upper(), "")
        val = collapse(str_test)
        if val < min_val:
            min_val = val

    print(min_val)

with open("input5.txt") as file:
    string = file.readlines()[0].strip()

    notdone = True
    spot = 0
    char1 = string[spot]
    while notdone:
        #print(spot)
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

    ## For Rotation
    #cont = True
    #while cont:
        #char1 = string[0]
        #char2 = string[len(string) - 1]
        #print(char1 +  " " + char2)
        #if char1.lower() == char2.lower() and char1 != char2:
            #string = string[1:len(string)-1]
        #else:
            #cont = False

    print("The remaining string is: " + str(len(string)) + " characters long.")

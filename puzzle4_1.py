import numpy as np

with open("input4.txt") as file:
    schedule = file.readlines()
    schedule = sorted(schedule)

    totals = dict()
    # dictionary with each guard as id storing total time asleep and which lines
    current_guard = 0
    current_sleep = 0
    for line in schedule:
        timeend = line.find(']')
        if line[timeend + 2: timeend + 7] == "Guard":
            current_guard = int(line[line.find('#') + 1: line.find('begin') - 1])
            if current_guard in totals:
                x = 0
            else:
                totals[current_guard] = np.full((1, 60), 0)
        else:
            time = int(line[line.find(':') + 1: line.find(':') + 3])
            if line[timeend + 2: timeend + 7] == "falls":
                current_sleep = time
            else:
                for i in list(range(current_sleep, time)):
                    totals[current_guard][0, i] += 1

    max_guard = 0
    max_time = 0
    max_minute = 0
    for guard in totals:
        total_time = 0
        curr_max_time = 0
        curr_max = 0
        for i, val in enumerate(totals[guard][0, :]):
            total_time += val
            if val > curr_max:
                curr_max = val
                curr_max_time = i
        if max_time < total_time:
            max_time = total_time
            max_guard = guard
            max_minute = curr_max_time


    print(int(max_guard) * max_minute)

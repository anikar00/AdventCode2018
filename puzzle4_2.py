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
    max_times = 0
    max_minute = 0
    for guard in totals:
        curr_max_minute = 0
        curr_max_times = 0
        for i, val in enumerate(totals[guard][0, :]):
            if val > curr_max_times:
                curr_max_times = val
                curr_max_minute = i
        if max_times < curr_max_times:
            max_times = curr_max_times
            max_guard = guard
            max_minute = curr_max_minute


    print(max_guard * max_minute)

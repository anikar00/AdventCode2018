with open("input7.txt") as file:
    instructions = file.readlines()

available = set()
order = ""
num_predecessors = {}
successors = {}
all_tasks = set()
task_times = {}
completed = 0

for item in instructions:
    first = item[item.find('m') - 2]
    second = item[item.find('c') - 2]

    all_tasks.add(first)
    all_tasks.add(second)

    if second in num_predecessors:
        num_predecessors[second] += 1
    else:
        num_predecessors[second] = 1

    if first in successors:
        successors[first].append(second)
    else:
        successors[first] = [second]

for i in range(26):
    task_times[chr(i + 65)] = 61 + i

for task in all_tasks:
    pred = num_predecessors.get(task, 0)
    if pred == 0:
        available.add(task)

needMoreTime = True
numWorkers = 5
workers = {} # time needed for each to finish their current task
for i in range(numWorkers):
    workers[i + 1] = {'time': 0, 'project': ''}
time = 0

while needMoreTime == True:
    time += 1
    for worker in workers:
        if workers[worker]['time'] == 0:
            if workers[worker]['project'] != '':
                task = workers[worker]['project']
                completed += 1
                for toadd in successors.get(task, []):
                    num_predecessors[toadd] -= 1
                    if num_predecessors[toadd] == 0:
                        available.add(toadd)
                workers[worker]['project'] = ''
            if len(sorted(available)) == 0:
                continue
            else:
                task = sorted(available)[0]
                available.remove(task)
                workers[worker]['time'] = task_times[task]
                workers[worker]['project'] = task
        workers[worker]['time'] -= 1
    if completed == len(all_tasks):
        needMoreTime = False


print("The total time needed is: " + str(time - 2) + " seconds.")

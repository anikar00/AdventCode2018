with open("input7.txt") as file:
    instructions = file.readlines()

available = set()
order = ""
num_predecessors = {}
successors = {}
all_tasks = set()

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

for task in all_tasks:
    pred = num_predecessors.get(task, 0)
    if pred == 0:
        available.add(task)

while len(order) < len(all_tasks):
    task = sorted(available)[0]
    order += task
    available.remove(task)
    for toadd in successors.get(task, []):
        num_predecessors[toadd] -= 1
        if num_predecessors[toadd] == 0:
            available.add(toadd)

print("The correct order is: " + order)

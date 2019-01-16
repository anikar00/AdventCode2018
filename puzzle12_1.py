with open("input12.txt") as file:
    lines = file.readlines()

state = list(lines[0][lines[0].find(':') + 2:-1])
rules = {}
for line in lines[2:]:
    rules[line[:line.find('=') - 1]] = line[line.find('>') + 2 ]

zero_index = 0
for gen in range(20):
    count = 0
    while state[count] == '.':
        count += 1
    if count <= 5:
        state = ['.'] * (5 - count) + state
        zero_index += (5 - count)
    count = 1
    while state[-count] == '.':
        count += 1
    if count <= 5:
        state = state + ['.'] * (6 - count)

    new_state = ['.', '.']
    for i in range(2, len(state) - 2):
        group = str(state[i - 2]) + str(state[i - 1]) + str(state[i]) + str(state[i + 1]) + str(state[i + 2])
        new_state.append(rules.get(group, '.'))
    new_state.append(['.', '.'])
    state = new_state

total = 0
for i, val in enumerate(state):
    index = i - zero_index
    if val == "#":
        total += index

print(total)

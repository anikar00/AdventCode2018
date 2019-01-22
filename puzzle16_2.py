import re

def addr(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] + vals[instr[2]]
    return end_vals

def addi(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] + instr[2]
    return end_vals

def mulr(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] * vals[instr[2]]
    return end_vals

def muli(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] * instr[2]
    return end_vals

def banr(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] & vals[instr[2]]
    return end_vals

def bani(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] & instr[2]
    return end_vals

def borr(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] | vals[instr[2]]
    return end_vals

def bori(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]] | instr[2]
    return end_vals

def setr(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = vals[instr[1]]
    return end_vals

def seti(instr, vals):
    end_vals = vals[:]
    end_vals[instr[3]] = instr[1]
    return end_vals

def gtir(instr, vals):
    end_vals = vals[:]
    if instr[1] > vals[instr[2]]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

def gtri(instr, vals):
    end_vals = vals[:]
    if instr[2] < vals[instr[1]]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

def gtrr(instr, vals):
    end_vals = vals[:]
    if vals[instr[1]] > vals[instr[2]]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

def eqir(instr, vals):
    end_vals = vals[:]
    if instr[1] == vals[instr[2]]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

def eqri(instr, vals):
    end_vals = vals[:]
    if vals[instr[1]] == instr[2]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

def eqrr(instr, vals):
    end_vals = vals[:]
    if vals[instr[1]] == vals[instr[2]]:
        end_vals[instr[3]] = 1
    else:
        end_vals[instr[3]] = 0
    return end_vals

with open("input16.txt") as file:
    input = file.readlines()
    tests = []
    program = []
    covered = 0
    for i in range(len(input)):
        if input[i].find('Before:') == 0:
            tests.append([list(map(int, re.findall("\d+", input[i]))),
                list(map(int, re.findall("\d+", input[i+1]))),
                list(map(int, re.findall("\d+", input[i+2])))])
            covered = i + 2
        elif input[i].strip() != '' and i > covered:
            program.append(list(map(int, re.findall("\d+", input[i]))))



operations = {addr:-1 , addi:-1 , mulr: -1 , muli: -1, banr: -1, bani: -1,
                    borr: -1, bori: -1, setr: -1, seti: -1, gtir: -1, gtri: -1,
                    gtrr: -1, eqir: -1, eqri: -1, eqrr: -1}
for test in tests:
    possibles = []
    for op in operations.keys():
        if test[2] == op(test[1], test[0]):
            possibles.append([op, test[1][0]])
    unknown = []
    for p in possibles:
        if operations[p[0]] == -1:
            unknown.append(p)
    if len(unknown) == 1:
        operations[unknown[0][0]] = unknown[0][1]

register = [0, 0, 0, 0]
ops = dict((v,k) for k,v in operations.items())
for p in program:
    register = ops[p[0]](p, register)

print(register[0])

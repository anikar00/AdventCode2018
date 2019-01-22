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
    for i in range(len(input)):
        if input[i].find('Before:') == 0:
            tests.append([list(map(int, re.findall("\d+", input[i]))),
                list(map(int, re.findall("\d+", input[i+1]))),
                list(map(int, re.findall("\d+", input[i+2])))])

operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

testSuccess = 0
for test in tests:
    success = 0
    for op in operations:
        if test[2] == op(test[1], test[0]):
            success += 1
    if success >= 3:
        testSuccess += 1

print(testSuccess)

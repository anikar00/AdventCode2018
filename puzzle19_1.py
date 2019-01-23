import re

def addr(instr, vals):
    vals[instr[3]] = vals[instr[1]] + vals[instr[2]]

def addi(instr, vals):
    vals[instr[3]] = vals[instr[1]] + instr[2]

def mulr(instr, vals):
    vals[instr[3]] = vals[instr[1]] * vals[instr[2]]

def muli(instr, vals):
    vals[instr[3]] = vals[instr[1]] * instr[2]

def banr(instr, vals):
    vals[instr[3]] = vals[instr[1]] & vals[instr[2]]

def bani(instr, vals):
    vals[instr[3]] = vals[instr[1]] & instr[2]

def borr(instr, vals):
    vals[instr[3]] = vals[instr[1]] | vals[instr[2]]

def bori(instr, vals):
    vals[instr[3]] = vals[instr[1]] | instr[2]

def setr(instr, vals):
    vals[instr[3]] = vals[instr[1]]

def seti(instr, vals):
    vals[instr[3]] = instr[1]

def gtir(instr, vals):
    if instr[1] > vals[instr[2]]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

def gtri(instr, vals):
    if instr[2] < vals[instr[1]]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

def gtrr(instr, vals):
    if vals[instr[1]] > vals[instr[2]]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

def eqir(instr, vals):
    if instr[1] == vals[instr[2]]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

def eqri(instr, vals):
    if vals[instr[1]] == instr[2]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

def eqrr(instr, vals):
    if vals[instr[1]] == vals[instr[2]]:
        vals[instr[3]] = 1
    else:
        vals[instr[3]] = 0

with open("input19.txt") as file:
    input = file.readlines()
    instructions = []
    ip = int(re.findall("\d+", input[0])[0])
    for i in range(1, len(input)):
      instructions.append([input[i][0:4]] + list(map(int, re.findall("\d+", input[i]))))

next = 0
operations = {'addr':addr , 'addi':addi , 'mulr': mulr , 'muli': muli, 'banr': banr, 'bani': bani,
                    'borr': borr, 'bori': bori, 'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri,
                    'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr}

registers = [0, 0, 0, 0, 0, 0]
while next < len(instructions):
    instruct = instructions[next]
    operations[instruct[0]](instruct, registers)
    registers[ip] += 1
    next = registers[ip]

print(registers)

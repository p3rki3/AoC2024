import AoCFramework as AoC

def get_combo(operand):
    match(operand):
        case 0, 1, 2, 3:
            return operand
        case 4:
            return RegA
        case 5:
            return RegB
        case 6:
            return RegC
        case 7:
            print("ERROR")
    return operand

def op0(operand):
    global IP, RegA, RegB, RegC, Output
    RegA = RegA // (2 ** get_combo(operand))

def op1(operand):
    global IP, RegA, RegB, RegC, Output
    RegB = RegB ^ operand

def op2(operand):
    global IP, RegA, RegB, RegC, Output
    RegB = get_combo(operand) % 8

def op3(operand):
    global IP, RegA, RegB, RegC, Output
    if RegA != 0:
        IP = operand - 1

def op4(operand):
    global IP, RegA, RegB, RegC, Output
    RegB = RegB ^ RegC

def op5(operand):
    global IP, RegA, RegB, RegC, Output
    RegB = get_combo(operand) % 8
    Output.append(RegB)

def op6(operand):
    global IP, RegA, RegB, RegC, Output
    RegB = RegA // (2 ** get_combo(operand))

def op7(operand):
    global IP, RegA, RegB, RegC, Output
    RegC = RegA // (2 ** get_combo(operand))
    
def run(regA):
    global IP, RegA, RegB, RegC, Output
    despatch = [op0, op1, op2, op3, op4, op5, op6, op7]
    RegA, RegB, RegC, IP, Output = regA, oldB, oldC, 0, []
    while IP < len(Prog):
        despatch[Prog[IP][0]](Prog[IP][1])
        IP += 1

def part_2(a=0, posn=0):
    if posn == len(rev_prog):
        return a
    for i in range(8):
        run(a*8 + i)
        if len(Output) and Output[0] == rev_prog[posn]:
            ret_val = part_2((a * 8 + i), posn + 1)
            if ret_val: 
                return ret_val
    return 0

Lines = AoC.Init("data/day17.txt", test=False)[0]
RegA = int(Lines[0][12:])
oldB = RegB = int(Lines[1][12:])
oldC = RegC = int(Lines[2][12:])
progints = [int(val) for val in Lines[4][9:].split(',')]
IP, Output, Prog, rev_prog = 0, [], [], progints[::-1]
for i in range(0, len(progints), 2):
    Prog.append((progints[i], progints[i+1]))
run(RegA)

AoC.verify('2,1,4,0,7,4,0,2,3', 258394985014171)
AoC.run(','.join((str(num) for num in Output)), part_2)

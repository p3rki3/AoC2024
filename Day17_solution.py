import AoCFramework as AoC

def run(regA):
    global Output
    RegA, RegB, RegC, IP, Output = regA, int(Lines[1][12:]), int(Lines[2][12:]), 0, []
    while IP < len(Prog):
        instr, operand = Prog[IP]
        match instr:
            case 0: RegA = RegA // (2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand])
            case 1: RegB = RegB ^ operand
            case 2: RegB = [operand, operand, operand, operand, RegA, RegB, RegC][operand] % 8
            case 3: IP = operand -1 if RegA!=0 else IP
            case 4: RegB = RegB ^ RegC
            case 5: Output.append(RegB := [operand, operand, operand, operand, RegA, RegB, RegC][operand] % 8)
            case 6: RegB = RegA // (2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand])
            case 7: RegC = RegA // (2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand])
        IP += 1

def part_1():
    run(int(Lines[0][12:]))
    return ','.join((str(num) for num in Output))

def part_2(regA=0, posn=0):
    if posn == len(progints): return regA
    for i in range(8):
        run(regA * 8 + i)
        if len(Output) and Output[0] == progints[-(posn + 1)]:
            ret_val = part_2((regA * 8 + i), posn + 1)
            if ret_val: return ret_val

Lines = AoC.Init("data/day17.txt")[0]
progints = [int(val) for val in Lines[4][9:].split(',')]
Prog = [(progints[i], progints[i+1]) for i in range(0, len(progints), 2)]
AoC.verify('2,1,4,0,7,4,0,2,3', 258394985014171)
AoC.run(part_1, part_2)

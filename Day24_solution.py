import AoCFramework as AoC

def part_1():
    global Wires, Logic
    lefttodo = len(Logic)
    while lefttodo > 0:
        for logic in Logic:
            if logic[4] > 0 and logic[0] in Wires and logic[1] in Wires:
                logic[4] = 0
                if logic[2] == 'AND': res = Wires[logic[0]] & Wires[logic[1]]
                elif logic[2] == 'OR': res = Wires[logic[0]] | Wires[logic[1]]
                else: res = Wires[logic[0]] ^ Wires[logic[1]]
                Wires[logic[3]] = res
                lefttodo -= 1
    ZWires = {wire for wire in Wires if wire[0] == 'z'}
    answer = ''
    for item in reversed(sorted(ZWires)):
        answer += str(Wires[item])
    return int(answer, 2)

def part_2():
    answer = []
    for logic in Logic:
        if logic[2] == 'AND' and logic[0][0] == 'x' and logic[1][0] == 'y':   # Rule 1
            if logic[3][0] == 'z' and logic[3] != 'z00':
                answer.append(logic[3])
                logic[5] = 1
        elif logic[2] == 'XOR' and logic[0][0] != 'x' and logic[1][0] != 'y' and logic[3][0] != 'z':   # Rule 2
            answer.append(logic[3])
            logic[5] = 1
        elif logic[3][0] == 'z' and logic[2] != 'XOR' and logic[3] != 'z45':  # Rule 3
            answer.append(logic[3])
            logic[5] = 1
        if logic[5] == 0 and logic[2] == 'AND' and logic[0][0] == 'x' and logic[1][0] == 'y' and logic[0] != 'x00':   # Rule 4
            found = False
            for logic2 in Logic:
                if logic2[2] == 'OR' and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                    found = True
            if found is not True:
                answer.append(logic[3])
        elif logic[5] == 0 and logic[2] == 'XOR' and logic[0][0] == 'x' and logic[1][0] == 'y' and logic[0] != 'x00':   # Rule 5
            found = False
            for logic2 in Logic:
                if logic2[2] == 'AND' and (logic[3] == logic2[0] or logic[3] == logic2[1]):
                    found = True
            if found is not True:
                answer.append(logic[3])
    return ','.join(sorted(answer))
    
Lines = AoC.Init("data/day24.txt", test=False, nolines=True).split('\n\n')
Wires, Logic = dict(), []
for line in Lines[0].split('\n'):
    wire, val = line.split(':')
    Wires[wire] = int(val.strip())
for line in Lines[1].split('\n'):
    wire1, op, wire2, _, wire3 = line.split(' ')
    if wire1 > wire2: wire1, wire2 = wire2, wire1
    Logic.append([wire1, wire2, op, wire3, 1, 0])

AoC.verify(64755511006320, 'djg,dsd,hjm,mcq,sbg,z12,z19,z37')
AoC.run(part_1, part_2)

# Second part was done in excel highlighting 8 nodes that didn't fit the pattern of everything else.
# Rule 1: any Xnn AND Ynn giving a znn node is in error and the znn node can be highlighted for swapping
# Rule 2: Any XOR operation should be either:
#  a)  Xnn XOR Ynn -> intermediate result except z00
#  b)  abc XOR def -> znn; any not giving rise to a znn should be highlighted for swapping
# Rule 3: Any znn that is NOT the result of an XOR operation should be highlighted for swapping
# Rule 4: Except for rules already highlighted as needing a swap, the intermediate result of x00 AND y00 should be an operand of one of the OR rules
# Rule 5: Except for rules already highlighted as needing a swap (rules 1-3), the intermediate result of x00 XOR y00 should be an operand of one of the AND rules

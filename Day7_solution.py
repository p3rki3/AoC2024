import AoCFramework as AoC
from itertools import product

def solve(opers):
    answer = 0
    for eq in Equations:
        res, inp, opsneeded, interim = eq[0], eq[1], len(eq[1]) - 1, 0
        operator_list = [list(opers) for _ in range(opsneeded)]
        for comb in product(*operator_list):
            interim = inp[0]
            for i in range(opsneeded):
                if comb[i] == '+':
                    interim += inp[i+1]
                elif comb[i] == '|':
                    interim = int(str(interim) + str(inp[i+1]))
                else:
                    interim *= inp[i+1]
            if interim == res:
                answer += res
                break
    return answer

Eqs_working = [line.split(':') for line in AoC.Init("data/day7.txt")[0]]
Equations = []
for eq in Eqs_working:
    res = int(eq[0])
    inplist = [int(num) for num in eq[1].split()]
    Equations.append((res, inplist))

AoC.verify(5512534574980, 328790210468594)
AoC.run(solve(['+', '*']), solve(['+', '*', '|']))

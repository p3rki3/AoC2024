import AoCFramework as AoC
from itertools import product

def solve(opers):
    answer = 0
    for eq in Equations:
        res, inp, opsneeded = eq[0], eq[1], len(eq[1]) - 1
        operator_list = [opers] * opsneeded
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

Equations = [(int(eq[0]), [int(num) for num in eq[1].split()]) for eq in [line.split(':') for line in AoC.Init("data/day7.txt")[0]]]
AoC.verify(5512534574980, 328790210468594)
AoC.run(solve(['+', '*']), solve(['+', '*', '|']))

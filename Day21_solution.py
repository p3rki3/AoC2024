import AoCFramework as AoC
from collections import Counter

def get_step_count(pad: dict, code: str, incr: int) -> Counter:
    (Ax, Ay), (Spx, Spy), count = pad["A"], pad[" "], Counter()
    for c in code:
        nxtx, nxty = pad[c]
        count[(nxtx - Ax, nxty - Ay, (nxtx == Spx and Ay == Spy) or (nxty == Spy and Ax == Spx))] += incr
        Ax, Ay = nxtx, nxty
    return count

def solve() -> tuple:
    part1 = part2 = 0
    for code in Lines:
        steps = get_step_count(keypad, code, 1)
        for depth in range(26):
            steps = sum((get_step_count(dirpad, ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if flag else 1] + "A", steps[(x, y, flag)]) for x, y, flag in steps), Counter())
            part1 += steps.total() * int(code[:3]) if depth == 2 else 0
        part2 += steps.total() * int(code[:3])
    return part1, part2

Lines = AoC.Init("data/day21.txt")[0]
keypad = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), ' ': (0, 3), '0': (1, 3), 'A': (2, 3)}
dirpad = {' ': (0, 0), '^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
AoC.verify(177814, 220493992841852)
AoC.run(solve())

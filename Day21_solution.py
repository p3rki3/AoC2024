import AoCFramework as AoC
from collections import Counter

def get_step_count(G: dict[complex, str], s: str, i=1):
    px, py = G["A"]
    bx, by = G[" "]
    count = Counter()
    for c in s:
        npx, npy = G[c]
        f = (npx == bx and py == by) or (npy == by and px == bx)
        count[(npx - px, npy - py, f)] += i
        px, py = npx, npy
    return count

def solve(depth):
    score = 0
    for code in Lines:
        steps = get_step_count(keypad, code)
        for _ in range(depth):
            steps = sum((get_step_count(dirpad, ("<" * -x + "v" * y + "^" * -y + ">" * x)[:: -1 if f else 1] + "A", steps[(x, y, f)]) for x, y, f in steps), Counter())
        score += steps.total() * int(code[:3])
    return score

Lines = AoC.Init("data/day21.txt")[0]
keypad = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
dirpad = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}
AoC.verify(177814, 220493992841852)
AoC.run(solve(3), solve(26))

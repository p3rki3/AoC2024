import AoCFramework as AoC
from collections import defaultdict
from math import prod

def get_quadrant_t100(p, v):
    p[0], p[1] = p[0] + v[0] * 100, p[1] + v[1] * 100
    x, y = p[0] % 101, p[1] % 103
    qx, qy = (x * 2) // 101, (y * 2) // 103
    return None if (x == 50 or y == 51) else (qx, qy)

def part_1():
    counts = defaultdict(int)
    for p, v in robots:
        q = get_quadrant_t100(p, v)
        if q is not None:
            counts[q] += 1
    return prod(counts.values())

def part_2():
    for i in range(101, 103 * 101 + 1):   # already done 100 iterations; assumes easter egg not in 1st 100
        posrobots = set()
        for p, v in robots:
            p[0], p[1] = p[0] + v[0], p[1] + v[1]
            posrobots.add((p[0] % 101, p[1] % 103))
        if len(posrobots) == len(robots): # assume easter egg is when all robots are in a different position
            return i
    return 0

robots = []
for line in AoC.Init("data/day14.txt")[0]:
    subline = line.split()
    (px, py) = (int(n) for n in subline[0].split('=')[1].split(','))
    (vx, vy) = (int(n) for n in subline[1].split('=')[1].split(','))
    robots.append([[px, py], [vx, vy]])

AoC.verify(226236192, 8168)
AoC.run(part_1, part_2)

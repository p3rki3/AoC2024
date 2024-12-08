from collections import defaultdict
from itertools import permutations, combinations
import AoCFramework as AoC

def part_1() -> int:
    antinodes = [[0 for _ in range(linelen)] for _ in range(numlines)]
    for _, pos in Antennas.items():
        for r, c in permutations(pos, 2):
            dist = (c[0] - r[0], c[1] - r[1])
            npos = r[0] - dist[0], r[1] - dist[1]
            if 0 <= npos[0] < numlines and 0 <= npos[1] < linelen:
                antinodes[npos[0]][npos[1]] = 1
    return sum(sum(row) for row in antinodes)

def part_2() -> int:
    antinodes = [[0 for _ in range(linelen)] for _ in range(numlines)]
    for _, pos in Antennas.items():
        for r, c in combinations(pos, 2):
            dist = (c[0] - r[0], c[1] - r[1])
            antinodes[r[0]][r[1]] = antinodes[c[0]][c[1]] = 1
            for npos in [(r[0] - dist[0], r[1] - dist[1], -dist[0], -dist[1]), (c[0] + dist[0], c[1] + dist[1], dist[0], dist[1])]:
                while 0 <= npos[0] < numlines and 0 <= npos[1] < linelen:
                    antinodes[npos[0]][npos[1]] = 1
                    npos = npos[0] + npos[2], npos[1] + npos[3], npos[2], npos[3]
    return sum(sum(row) for row in antinodes)

Lines, numlines, linelen = AoC.Init("data/day8.txt", test=False)
Antennas = defaultdict(list)
for row, line in enumerate(Lines):
    for col, char in enumerate(line):
        if char != '.':
            Antennas[char].append((row, col))

AoC.verify(341, 1134)
AoC.run(part_1, part_2)
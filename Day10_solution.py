from collections import namedtuple
import AoCFramework as AoC

def walk_path(x, y, previous, end_of_trail):
    current = Grid[y][x] if 0 <= x < linelen and 0 <= y < numlines else None
    if current is None or current - previous != 1:
        return
    if current == 9:
        end_of_trail.append(Point(x, y))
        return
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        walk_path(x + dx, y + dy, current, end_of_trail)

def solve():
    global Grid
    Grid = [[int(ch) for ch in line] for line in Lines]
    Poss_starts = [ Point(x, y) for y, line in enumerate(Grid) for x, c in enumerate(line) if c == 0 ]
    part1, part2 = [], []

    for p in Poss_starts:
        end_of_trail = []
        walk_path(p.x, p.y, -1, end_of_trail)
        part1.append(len(set(end_of_trail)))
        part2.append(len(end_of_trail))
    return sum(part1), sum(part2)

Lines, numlines, linelen = AoC.Init("data/day10.txt", test=False, nolines=False, isnumlist=False, printme=False, pad=0, padchar=' ')
Point, Poss_starts, Grid = namedtuple("Point", ("x", "y")), [], []
AoC.verify(607, 1384)
AoC.run(solve())

import AoCFramework as AoC
from collections import deque
from itertools import product

def solve():
    part1, part2, Dirns, AlreadySeen = 0, 0, [(1, 0),(0, 1),(-1, 0),(0, -1)], set()
    for r, c in product(range(numlines), range(linelen)):
        if (r, c) in AlreadySeen:
            continue

        area, perim, sides, queue, PerimDict = 0, 0, 0, deque([(r, c)]), dict()
        while queue:
            r2, c2 = queue.popleft()
            if (r2, c2) in AlreadySeen:
                continue
            AlreadySeen.add((r2, c2))
            area += 1
            for dr, dc in Dirns:
                nextr, nextc = r2 + dr, c2 + dc
                if 0 <= nextr < numlines and 0 <= nextc < linelen and Lines[nextr][nextc] == Lines[r2][c2]:
                    queue.append((nextr, nextc))
                else:
                    perim += 1
                    if (dr, dc) not in PerimDict:
                        PerimDict[(dr, dc)] = set()
                    PerimDict[(dr, dc)].add((r2, c2))

        for perims in PerimDict.values():
            AlreadySeenPerim = set()
            for (r, c) in perims:
                if (r, c) not in AlreadySeenPerim:
                    sides += 1
                    queue2 = deque([(r, c)])
                    while queue2:
                        r2, c2 = queue2.popleft()
                        if (r2, c2) in AlreadySeenPerim:
                            continue
                        AlreadySeenPerim.add((r2, c2))
                        for dr, dc in Dirns:
                            nextr, nextc = r2 + dr, c2 + dc
                            if (nextr, nextc) in perims:
                                queue2.append((nextr, nextc))

        part1, part2 = part1 + area * perim, part2 + area * sides
    return part1, part2

Lines, numlines, linelen = AoC.Init("data/day12.txt")
AoC.verify(1375476, 821372)
AoC.run(solve())

import AoCFramework as AoC
from itertools import product

def solve() -> tuple:
    part1 = part2 = 0
    grid = {i + j * 1j: char for i,line in enumerate(Lines) for j,char in enumerate(line) if char != '#'}
    startpt, = (p for p in grid if grid[p] == 'S')    # unpack the generator; assumes only one 'S' cell
    queue, distance = [startpt], {startpt: 0}
    for posn in queue:
        for nextpos in posn - 1, posn + 1, posn - 1j, posn + 1j:
            if nextpos in grid and nextpos not in distance:
                distance[nextpos] = distance[posn] + 1
                queue.append(nextpos)
    for pt1, pt2 in product(distance, repeat=2):
        cheatlen = abs((pt1 - pt2).real) + abs((pt1 - pt2).imag)
        if cheatlen == 2 and distance[pt1] - distance[pt2] - cheatlen >= 100: part1 += 1
        if cheatlen < 21 and distance[pt1] - distance[pt2] - cheatlen >= 100: part2 += 1
    return (part1, part2)

Lines = AoC.Init("data/day20.txt")[0]
AoC.verify(1351, 966130)
AoC.run(solve())

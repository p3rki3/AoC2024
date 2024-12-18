import AoCFramework as AoC
from collections import deque

def find_path(grid):
    start, end = (0, 0), (maxx - 1, maxy - 1)
    if grid[start[0]][start[1]] == '#' or grid[end[0]][end[1]] == '#':
        return None

    queue, visited, dirs = deque([(start, [start])]), [[False] * maxy for _ in range(maxx)], [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited[start[0]][start[1]] = True
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.' and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

def part_1(blocks = 1024):
    Grid = [['.' for _ in range(maxy)] for _ in range(maxx)]
    for i in range(min(blocks, len(Lines))):
        (x, y) = (int(num) for num in Lines[i].split(','))
        Grid[y][x] = '#'
    return (len(path) - 1) if (path := find_path(Grid)) else None

def part_2():
    lower, upper = 1024, len(Lines)
    while True:
        testval = lower + (upper - lower) // 2
        if testval == lower:
            return Lines[lower]
        elif part_1(testval) == None:
            upper = testval
        else:
            lower = testval

Lines, maxx, maxy = AoC.Init("data/day18.txt", test=False)[0], 71, 71
AoC.verify(380, '26,50')
AoC.run(part_1, part_2)

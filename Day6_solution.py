import AoCFramework as AoC

def run(obstacle_x=None,obstacle_y=None):
    x, y = start
    dirptr, visited, visited2 = 0, set(),set()
    visited.add((x, y))
    visited2.add((x, y, dirptr))
    while True:
        dx, dy = Dirns[dirptr]
        if obstacle_x and x != obstacle_x and y != obstacle_y: 
            k = Dist[y][x]
            while k >= 1:
                x += k * dx
                y += k * dy
                k = Dist[y][x]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= numlines or ny < 0 or ny >= linelen:
            return visited, False
        if Lines[ny][nx] == "#" or (nx == obstacle_x and ny == obstacle_y):
            dirptr = (dirptr + 1) % 4
        else:
            x, y = nx, ny
            if not obstacle_x:visited.add((x,y))
            if (x, y, dirptr) in visited2:
                return visited, True
            visited2.add((x, y, dirptr))

Lines, numlines, linelen = AoC.Init("data/day6.txt")
Dirns = ((0, -1), (1, 0), (0, 1), (-1, 0))
Dist = [[min(abs(x), abs(numlines - 1 - x), abs(y), abs(linelen - 1 - y)) for x in range(numlines)] for y in range(linelen)]
for y in range(linelen):
    for x in range(linelen):
        if Lines[y][x] == "^": 
            start = (x, y)
        for k in range(linelen):
            if Lines[y][k] == "#":
                Dist[y][x] = min(Dist[y][x],abs(k-x)-1)
            if Lines[k][x] == "#":
                Dist[y][x] = min(Dist[y][x],abs(k-y)-1)

Visited = run()[0]
AoC.verify(4374, 1705)
AoC.run(len(Visited), sum(run(x,y)[1] for x,y in Visited))

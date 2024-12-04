import AoCFramework as AoC

def part_1():
    count, dirns = 0, [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    for x in range(3, numlines+3):
        for y in range(3, linelen+3):
            for dx, dy in dirns:
                if Lines[y][x] == 'X' and Lines[y+dy][x+dx] == 'M' and Lines[y+dy*2][x+dx*2] == 'A' and Lines[y+dy*3][x+dx*3] == 'S':
                    count += 1
    return count

def part_2():
    count = 0
    for x in range(3, numlines+3):
        for y in range(3, linelen+3):
            if Lines[y+1][x+1] == 'A':
                if ((Lines[y][x] == 'M' and Lines[y+2][x+2] == "S") or (Lines[y][x] == 'S' and Lines[y+2][x+2] == "M")) and ((Lines[y+2][x] == 'M' and Lines[y][x+2] == "S") or (Lines[y+2][x] == 'S' and Lines[y][x+2] == "M")):
                    count += 1                    
    return count

Lines, numlines, linelen = AoC.Init("data/day4.txt", pad=3, padchar=' ')
AoC.verify(2618, 2011)
AoC.run(part_1, part_2)

import AoCFramework as AoC

def test_line(line) -> bool:
    dirn, lastnum, report = 0, 0, True
    for num in line:
        if lastnum > 0:
            diff = num - lastnum
            absdiff = abs(diff)
            if dirn == 0:
               dirn = 1 if diff > 0 else -1
            report &= (1 <= absdiff <= 3) and (dirn * diff > 0)
        lastnum = num
    return report

def test_line2(line) -> bool:
    isnowsafe = False
    for i in range(len(line)):
        isnowsafe |= test_line(line[:i] + line[i+1:])
    return isnowsafe

Levels = [[int(level) for level in line.split()] for line in AoC.Init("data/day2.txt")[0]]
AoC.verify(383, 436)
part_1 = sum(1 if test_line(line) else 0 for line in Levels)
part_2 = sum(1 if test_line2(line) else 0 for line in Levels)
AoC.run(part_1, part_2)

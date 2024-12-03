import AoCFramework as AoC

def test_line(line) -> bool:
    dirn, report = line[-1] - line[0], True
    for i in range(len(line) - 1):
        report &= (1 <= abs(line[i+1] - line[i]) <= 3) and (dirn * (line[i+1] - line[i]) > 0)
    return report

def test_line2(line) -> bool:
    for i in range(len(line)):
        if test_line(line[:i] + line[i+1:]):
            return True
    return False

Levels = [[int(level) for level in line.split()] for line in AoC.Init("data/day2.txt")[0]]
AoC.verify(383, 436)
AoC.run(sum(test_line(line) for line in Levels), sum(test_line2(line) for line in Levels))

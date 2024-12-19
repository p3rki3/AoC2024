import AoCFramework as AoC

def match_pattern(pattern: str) -> int:
    if pattern:
        ret_val = 0
        if pattern in SubPattern:
            return SubPattern[pattern]
        for cloth in Cloth:
            ret_val += match_pattern(pattern[len(cloth):]) if pattern.startswith(cloth) else 0
        SubPattern[pattern] = ret_val
        return ret_val
    return 1

def solve() -> tuple:
    part1 = part2 = 0
    for pattern in Patterns:
        pattern_match_count = match_pattern(pattern)
        part2 += pattern_match_count
        part1 += 1 if pattern_match_count > 0 else 0
    return part1, part2

Lines = AoC.Init("data/day19.txt", test=False)[0]
Cloth, Patterns, SubPattern = [c.strip() for c in Lines[0].split(',')], Lines[2:], dict()
AoC.verify(347, 919219286602165)
AoC.run(solve())

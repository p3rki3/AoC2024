import AoCFramework as AoC

def match_pattern(pattern: str) -> int:
    if pattern:
        if pattern not in SubPattern:
            SubPattern[pattern] = sum((match_pattern(pattern[len(cloth):]) if pattern.startswith(cloth) else 0) for cloth in Cloth)
        return SubPattern[pattern]
    return 1

Lines = AoC.Init("data/day19.txt", test=False)[0]
Cloth, Patterns, SubPattern = Lines[0].split(', '), Lines[2:], dict()
AoC.verify(347, 919219286602165)
AoC.run(sum(match_pattern(pattern) > 0 for pattern in Patterns), sum(SubPattern[pattern] for pattern in Patterns))

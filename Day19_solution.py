import AoCFramework as AoC

def match_pattern(pattern: str) -> int:
    if pattern:
        if pattern in SubPattern:
            return SubPattern[pattern]
        ret_val = sum((match_pattern(pattern[len(cloth):]) if pattern.startswith(cloth) else 0) for cloth in Cloth)
        SubPattern[pattern] = ret_val
        return ret_val
    return 1

Lines = AoC.Init("data/day19.txt", test=False)[0]
Cloth, Patterns, SubPattern = Lines[0].split(', '), Lines[2:], dict()
AoC.verify(347, 919219286602165)
AoC.run(sum(1 if match_pattern(pattern) > 0 else 0 for pattern in Patterns), sum(SubPattern[pattern] for pattern in Patterns))

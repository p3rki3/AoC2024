import re
import AoCFramework as AoC

Line = AoC.Init("data/day3.txt", nolines=True)
AoC.verify(190604937, 82857512)

def part_1(data=Line) -> int:
    answer = 0
    for match in re.findall(r'mul\(\d+,\d+\)', data):
        nums = match[4:-1].split(',')
        answer += int(nums[0]) * int(nums[1])
    return answer

def part_2() -> int:
    answer = 0
    for subl in Line.split("do()"):
        sublines2 = subl.split("don't()")
        answer += part_1(sublines2[0])
    return answer

AoC.run(part_1, part_2)
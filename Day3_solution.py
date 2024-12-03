import re
import AoCFramework as AoC

def part_1():
    answer = 0
    for match in re.findall(pattern, data):
        nums = match[4:-1].split(',')
        answer += int(nums[0]) * int(nums[1])
    return answer

def part_2():
    answer = 0
    for subl in data.split("do()"):
        sublines2 = subl.split("don't()")
        for match in re.findall(pattern, sublines2[0]):
            nums = match[4:-1].split(',')
            answer += int(nums[0]) * int(nums[1])
    return answer

data = AoC.Init("data/day3.txt", nolines=True)
pattern = r'mul\(\d+,\d+\)'
AoC.verify(190604937, 82857512)
AoC.run(part_1, part_2)




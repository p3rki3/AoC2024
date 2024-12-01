import AoCFramework as AoC

nums = [line.split() for line in AoC.Init("data/day1.txt")[0]]
N1, N2 = sorted([int(num[0]) for num in nums]), sorted([int(num[1]) for num in nums])
part_1 = part_2 = 0

for i in range(len(N1)):
    part_1 += abs(N1[i] - N2[i])
    part_2 += N1[i] * N2.count(N1[i])

AoC.verify(1151792, 21790168)
AoC.run(part_1, part_2)
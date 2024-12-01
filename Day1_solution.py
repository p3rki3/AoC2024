import AoCFramework as AoC

nums = [line.split() for line in AoC.Init("data/day1.txt")[0]]
N1, N2, lenN1 = sorted([int(num[0]) for num in nums]), sorted([int(num[1]) for num in nums]), len(nums)
AoC.verify(1151792, 21790168)
AoC.run(sum(abs(N1[i] - N2[i]) for i in range(lenN1)), sum(N1[i] * N2.count(N1[i]) for i in range(lenN1)))


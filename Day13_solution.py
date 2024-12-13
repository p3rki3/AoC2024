import AoCFramework as AoC
import numpy as np

Lines, numlines, _ = AoC.Init("data/day13.txt")
answer = [0, 0]
for i in range((numlines // 4 + 1)):
    A = (int(Lines[i*4].split('+')[1].split(',')[0]), int(Lines[i*4].split('+')[2]))
    B = (int(Lines[i*4+1].split('+')[1].split(',')[0]), int(Lines[i*4+1].split('+')[2]))
    P = (int(Lines[i*4+2].split('=')[1].split(',')[0]), int(Lines[i*4+2].split('=')[2]))
    for i, addon in enumerate([0, 10000000000000]):
        x, y = np.linalg.solve(np.array([[A[0], B[0]], [A[1], B[1]]]), np.array([P[0] + addon, P[1] + addon]))
        if round(x, 2).is_integer() and round(y, 2).is_integer():
            answer[i] += int(round(x, 0) * 3 + round(y, 0))

AoC.verify(28138, 108394825772874)
AoC.run(answer[0], answer[1])

import AoCFramework as AoC
import numpy as np

def solve(part=0):
    tokens = 0
    for A, B, P in Games:
        x1, y1, z1 = A[0], B[0], P[0] + part
        x2, y2, z2 = A[1], B[1], P[1] + part
        x, y = np.linalg.solve(np.array([[x1, y1], [x2, y2]]), np.array([z1, z2]))
        if round(x, 2).is_integer() and round(y, 2).is_integer():
            tokens += int(round(x, 0) * 3 + round(y, 0))
    return tokens

Lines, numlines, _ = AoC.Init("data/day13.txt", test=False)
Games = []
for i in range((numlines // 4 + 1)):
    A = (int(Lines[i*4].split('+')[1].split(',')[0]), int(Lines[i*4].split('+')[2]))
    B = (int(Lines[i*4+1].split('+')[1].split(',')[0]), int(Lines[i*4+1].split('+')[2]))
    P = (int(Lines[i*4+2].split('=')[1].split(',')[0]), int(Lines[i*4+2].split('=')[2]))
    Games.append((A, B, P))

AoC.verify(28138, 108394825772874)
AoC.run(solve(), solve(10000000000000))

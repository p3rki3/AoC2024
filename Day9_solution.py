import sys
import AoCFramework as AoC
from collections import deque

def solve(part=1):
    fileid, posn, files, freespace, compacted = 0, 0, deque([]), deque([]), []

    for i, ch in enumerate(Lines):
        if i % 2 == 0:
            if part == 2:
                files.append((posn, fileid, int(ch)))
            for i in range(int(ch)):
                compacted.append(fileid)
                if part == 1:
                    files.append((posn, fileid, 1))
                posn += 1
            fileid += 1
        else:
            freespace.append((posn, int(ch)))
            for i in range(int(ch)):
                posn += 1
                compacted.append(None)

    for (posn, fileid, size) in reversed(files):
        for i, (emptyposn, emptysize) in enumerate(freespace):
            if emptyposn < posn and size <= emptysize:
                for j in range(size):
                    compacted[posn + j] = None
                    compacted[emptyposn + j] = fileid
                freespace[i] = (emptyposn + size, emptysize - size)
                break

    return sum(i * fileid for i, fileid in enumerate(compacted) if fileid is not None)

Lines = AoC.Init("data/day9.txt", nolines=True, test=False)
AoC.verify(6346871685398, 6373055193464)
AoC.run(solve(), solve(2))

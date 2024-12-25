import AoCFramework as AoC

def blocktonum(block: list) -> list:
    ret_num = []
    for j in range(5):
        num = 0
        for i in range(1,6):
            num += 1 if block[i][j] == '#' else 0
        ret_num.append(num)
    return ret_num

Blocks = AoC.Init("data/day25.txt", test=False, nolines=True).split('\n\n')
Locks, Keys = [], []
for blocks in Blocks:
    block = blocks.split('\n')
    if block[0][0] == '#':   # Its a lock
        Locks.append(blocktonum(block))
    else:
        Keys.append(blocktonum(block))

part_1 = 0
for lock in Locks:
    for key in Keys:
        doesfit = True
        for i in range(len(lock)):
            if lock[i] + key[i] > 5:
                doesfit = False
        part_1 += 1 if doesfit is True else 0

AoC.verify(None, 'N/A')
AoC.run(part_1, 'N/A')

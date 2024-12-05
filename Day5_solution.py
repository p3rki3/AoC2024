import AoCFramework as AoC
from collections import defaultdict
from graphlib import TopologicalSorter

part_1, part_2, Orders = 0, 0, defaultdict(list)

for line in AoC.Init("data/day5.txt")[0]:
    if '|' in line:
        before, after = line.split("|")
        Orders[before].append(after)
    elif len(line) > 0:
        pages = line.split(",")
        topsort = TopologicalSorter({k:v for k, v in Orders.items() if k in pages})
        ordered = list(topsort.static_order())[::-1]
        mp = {n:i for i, n in enumerate(ordered)} 
        newpages = sorted(pages, key=lambda n: mp[n])
        mid_num = int(newpages[len(pages) // 2])
        if newpages == pages:
            part_1 += mid_num
        else:
            part_2 += mid_num

AoC.verify(4609, 5723)
AoC.run(part_1, part_2)

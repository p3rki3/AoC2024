import AoCFramework as AoC
from collections import defaultdict
from graphlib import TopologicalSorter

part_1, part_2, Orders = 0, 0, defaultdict(list)

for line in AoC.Init("data/day5.txt")[0]:
    if '|' in line:
        before, after = line.split("|")
        Orders[before].append(after)
    elif ',' in line:
        Pages = line.split(",")
        topsort = TopologicalSorter({x:y for x, y in Orders.items() if x in Pages})
        sortkey = {num:count for count, num in enumerate(list(topsort.static_order())[::-1]) if num in Pages}
        sortedpages = sorted(Pages, key=lambda n: sortkey[n])
        mid_num = int(sortedpages[len(Pages) // 2])
        if sortedpages == Pages:
            part_1 += mid_num
        else:
            part_2 += mid_num

AoC.verify(4609, 5723)
AoC.run(part_1, part_2)

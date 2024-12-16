import AoCFramework as AoC
import networkx as nx

def part_1():
    return nx.shortest_path_length(Grid, Start, "end", weight="weight")

def part_2():
    return len({z for path in nx.all_shortest_paths(Grid, Start, "end", weight="weight") for z, _ in path[:-1]})

def process_file():
    global Grid, Start
    for i, line in enumerate(Lines):
        for j, char in enumerate(line):
            z = i + 1j * j
            match char:
                case '#':
                    continue
                case 'S':
                    Start = (z, 1j)
                case 'E':
                    End = z
            for dz in Dirns:
                Grid.add_node((z, dz))
    for z, dz in Grid.nodes:
        if (z + dz, dz) in Grid.nodes:
            Grid.add_edge((z, dz), (z + dz, dz), weight=1)
        for rot in -1j, 1j:
            Grid.add_edge((z, dz), (z, dz * rot), weight=1000)
    for dz in Dirns:
        Grid.add_edge((End, dz), "end", weight=0)

Lines, Dirns, Grid, Start = AoC.Init("data/day16.txt")[0], (1, -1, 1j, -1j), nx.DiGraph(), None
process_file()
AoC.verify(75416, 476)
AoC.run(part_1, part_2)

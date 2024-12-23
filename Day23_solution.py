import AoCFramework as AoC
import networkx as nx

Lines = AoC.Init("data/day23.txt")[0]
Graph = nx.Graph(line.split("-") for line in Lines)
cliques = list(nx.enumerate_all_cliques(Graph))

AoC.verify(1423, 'gt,ha,ir,jn,jq,kb,lr,lt,nl,oj,pp,qh,vy')
AoC.run(sum(len(c) == 3 and any(x[0] == 't' for x in c) for c in cliques), ",".join(sorted(cliques[-1])))

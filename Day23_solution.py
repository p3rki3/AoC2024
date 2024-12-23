import AoCFramework as AoC
import networkx as nx

cliques = list(nx.enumerate_all_cliques(nx.Graph(line.split('-') for line in AoC.Init('data/day23.txt')[0])))
AoC.verify(1423, 'gt,ha,ir,jn,jq,kb,lr,lt,nl,oj,pp,qh,vy')
AoC.run(sum(len(clq) == 3 and any(node[0] == 't' for node in clq) for clq in cliques), ','.join(sorted(cliques[-1])))

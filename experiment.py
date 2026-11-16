import networkx as nx
G = nx.DiGraph(nx.path_graph(4))
pr = nx.pagerank(G, alpha=0.9)

print(pr)
import networkx as nx

def find_impostor(edgelist, pseudocenters):
    G = nx.Graph()
    G.add_edges_from(edgelist)
    min_degree = len((G.nodes()))
    res = pseudocenters[0]
    for center in pseudocenters:
        subgraph = nx.ego_graph(G,center)
        current_degree = len(set(subgraph.nodes()))
        if min_degree > current_degree:
            min_degree = current_degree
            res = center
    return res

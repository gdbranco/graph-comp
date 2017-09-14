"""
vai fazer uns treco
"""
import math
import matplotlib
import graph_tool.all as gt
import utils as ut
from pprint import pprint
# from pprint import pprint
# from time import time


def sort_nodes(tupla):
    """
    Sort nodes based on score
    """
    vertex = tupla[1]
    return -vertex[0], -vertex[1]

def score_func(network):
    """
    Devolve o score de cada no na network
    """
    return dict([(v[0], len(v[1])) for v in network.items()])

def bfs(graph, start):
    """
    Roda BFS e devolve uma floresta
    """
    queue = list()
    visited = set()
    queue.append(start)
    forest_edges = list()
    while queue:
        node = queue.pop(0)
        visited.add(node)
        for adjacent in graph[node]:
            if (adjacent, node) not in forest_edges and (node, adjacent) not in forest_edges:
                forest_edges.append((node, adjacent))
            if adjacent not in visited:
                visited.add(adjacent)
                if adjacent in graph:
                    queue.append(adjacent)
    return forest_edges, list(visited)

# retornar o set de visitados
# pegar o score
# edges

def sort_forests(forests):
    """
    Ordena a floresta pelo tamanho da mesma
    """
    return -len(forests)

def alg(network):
    """
    Run BFS for the entire network
    """
    num_nodes = len(list(network))
    output = {}
    visited_nodes = set()
    score_table = score_func(network)
    for node in network.keys():
        if node not in visited_nodes:
            # busco a floresta (e atualizo lista de nos visitados)
            forest_edges, forest = bfs(network, node)
            visited_nodes.update(forest)

            # ordenar a floresta pelo score de cada no
            forest = [(node, score_table[node]) for node in forest]
            forest = sorted(forest, key=lambda x: -x[1])
            ## calcubBFSlar score
            ##SCORE BASEADO NO GRAPH-TOOL
            grafo = gt.Graph(directed=False)
            pprint(forest_edges)
            grafo.add_edge_list(forest_edges)
            for node in grafo.vertices():
                if node.out_degree() == 0:
                    grafo.remove_vertex(node)
            gt.graph_draw(grafo, vertex_text=grafo.vertex_index, vertex_font_size=18, output_size=(1000,1000))
            # for v in vp:
            #     print (v)
            #SCORE NOSSO
            forest_size = len(forest)
            for node, score in forest:
                score = score * (forest_size / num_nodes)
                output[node] = score
                forest_size -= 1
    return sorted(output.items(), key=lambda x: -x[1])


if __name__ == "__main__":
    NET_NAME = "real2";
    print("Read all nodes")
    REDE = ut.import_netGT(NET_NAME)
    print("Adding data to graph")
    GRAFO = gt.Graph(directed=False)
    GRAFO.add_edge_list(REDE)
    print("Running pagerank")
    pr = gt.pagerank(GRAFO)
    pr = list(pr)
    print("Printing pagerank")
    _pr = list()
    index = 0
    for v in pr:
        _pr.append((index, v))
        index+=1
    del pr
    _pr = sorted(_pr, key=lambda x: -x[1])
    pprint(_pr[:10])
    
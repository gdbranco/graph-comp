"""
vai fazer uns treco
"""
import math
import numpy as np
import graph_tool.all as gt
from pprint import pprint


def import_net(filename):
        print(filename)
        mt = np.genfromtxt('networks/' + filename + '.csv',delimiter=',').astype(np.int32)
        
        # initialize V
        max_node = np.max(mt)
        vertices = max_node+1
        edges = list()

        # create adjacency list
        for row in mt[:1000]:
            node1 = row[0]
            node2 = row[1]
            edges.append((node1,node2))

        # assert (self.V == len(self.graph), "Numero de nos incorreto"

        print("ADD TODOS EDGES")
        return vertices, edges

def export_net(results, network_name, file_out, first=True):
    """ Export to format required by competition 
        Required: optimize/clean last if, redundancy """

    if first:
        f = open("./Results/" + file_out, 'w')

        # write headers
        f.write('NetID,')
        for i in range(1, 500):
            f.write('nodeID' + str(i) + ',')
        f.write('nodeID500')

    else:
        f = open(file_out, 'a')

    f.write('\n')
    # write each row
    counter = 1
    for tup in results:
        node = tup[0]
        if counter == 1:
            # add column header when counter is 1
            f.write(network_name + ',')
            counter += 1
        if counter == 501:
            f.write(str(node))
            f.write('\n')
            # reset counter at 500
            counter = 1
        else:
            f.write(str(node) + ',')
            counter += 1
            
    # calculate how much padding is required to be added
    padding = 0
    mod = len(results) % 500
    if mod != 0:
        padding = 500 - mod

    # add padding to last row
    for i in range(padding-1):
        f.write(',')

    f.close()


    print("Network " + network_name + " exported successfully.")

if __name__ == "__main__":
    GRAFO = gt.Graph(directed=False)
    network_name = "model1"
    num_v, edges = import_net(network_name)
    rvertices = list()
    redges = list()
    print("CREATING GRAPH-TOOLS GRAPH")
    for i in range(0,num_v):
        rvertices.append(GRAFO.add_vertex())
    for edge in edges:
        redges.append(GRAFO.add_edge(edge[0],edge[1]))
    # print("PAGE RANK")
    # pr = gt.pagerank(GRAFO)
    # _pr = list()
    # index = 0
    # for v in pr:
    #     _pr.append((index, v))
    #     index+=1
    # del pr
    # _pr = sorted(_pr, key=lambda x: -x[1])
    # pprint(_pr)
    print("BEETWENNESS")
    vb, eb = gt.betweenness(GRAFO)
    _vb = list()
    index = 0
    for v in vb:
        _vb.append((index,v))
        index+=1
    del vb
    _vb = sorted(_vb, key=lambda x:-x[1])
    pprint(_vb)
    export_net(_vb,network_name,"{}{}".format(network_name,".csv"), first=True)
    # print("CLOSENESS")
    # vc = gt.closeness(GRAFO)
    # _vc = list()
    # index = 0
    # for v in vc:
    #     _vc.append((index,v))
    #     index+=1
    # del vc
    # _vc = sorted(_vc,key=lambda x:-x[1])
    # pprint(_vc)
    # print("EIGENVECTOR")
    # evalue, evector = gt.eigenvector(GRAFO)
    # _evector = list()
    # index = 0
    # for v in evector:
    #     _evector.append((index,v))
    #     index+=1
    # del evector
    # _evector = sorted(_evector, key=lambda x:-x[1])
    # pprint(_evector)
    # print("KATZ")
    # kv = gt.katz(GRAFO)
    # _kv = list()
    # index = 0
    # for v in kv:
    #     _kv.append((index,v))
    #     index+=1
    # del kv
    # _kv = sorted(_kv, key=lambda x:-x[1])
    # pprint(_kv)
    # NET_NAME = "real2";
    # print("Read all nodes")
    # REDE = ut.import_netGT(NET_NAME)
    # print("Adding data to graph")
    # GRAFO = gt.Graph(directed=False)
    # GRAFO.add_edge_list(REDE)
    # print("#Running closeness")
    # vc = gt.closeness(GRAFO)
    # vc = list(vc)
    # _vc = list()
    # print("#Printing closeness")
    # index = 0
    # for v in vc:
    #     _vc.append((index,v))
    #     index+=1
    # del vc
    # _vc = sorted(_vc, key=lambda x: -x[1])
    # pprint(_vc[:10])
    ###BETWEENNESS
    # print("#Running betweenness")
    # vb, eb = gt.betweenness(GRAFO)
    # vb = list(vb)
    # _vb = list()
    # print("#Printing betweenness")
    # index = 0
    # for v in vb:
    #     _vb.append((index,v))
    #     index+=1
    # del vb
    # _vb = sorted(_vb, key=lambda x: -x[1])
    # pprint(_vb[:10])
    ##EIGENVECTOR
    # print("Running eigen")
    # ee, x = gt.eigenvector(GRAFO)
    # print("Printing eigen")
    # _ee = list()
    # index = 0
    # for v in x:
    #     _ee.append((index,v))
    #     index+=1
    # del x
    # _ee = sorted(_ee, key=lambda x: -x[1])
    # pprint(ee)
    # pprint(_ee[:10])
    ###PAGE RANK
    # print("Running pagerank")
    # pr = gt.pagerank(GRAFO)
    # pr = list(pr)
    # print("Printing pagerank")
    # _pr = list()
    # index = 0
    # for v in pr:
    #     _pr.append((index, v))
    #     index+=1
    # del pr
    # _pr = sorted(_pr, key=lambda x: -x[1])
    # pprint(_pr[:10])
    
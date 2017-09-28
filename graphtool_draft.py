"""
vai fazer uns treco
"""
import math
import matplotlib
import graph_tool.all as gt
import utils as ut
from pprint import pprint

if __name__ == "__main__":
    GRAFO = gt.Graph(directed=False)
    v = list()
    e = list()
    for i in range(0,9):
        v.append(GRAFO.add_vertex())
    e.append(GRAFO.add_edge(v[0],v[1]))
    e.append(GRAFO.add_edge(v[0],v[2]))
    e.append(GRAFO.add_edge(v[1],v[2]))
    e.append(GRAFO.add_edge(v[1],v[5]))
    e.append(GRAFO.add_edge(v[2],v[3]))
    e.append(GRAFO.add_edge(v[2],v[4]))
    e.append(GRAFO.add_edge(v[2],v[5]))
    e.append(GRAFO.add_edge(v[2],v[6]))
    e.append(GRAFO.add_edge(v[5],v[6]))
    e.append(GRAFO.add_edge(v[5],v[8]))
    e.append(GRAFO.add_edge(v[6],v[8]))
    e.append(GRAFO.add_edge(v[6],v[7]))
    e.append(GRAFO.add_edge(v[6],v[4]))
    e.append(GRAFO.add_edge(v[6],v[3]))
    e.append(GRAFO.add_edge(v[3],v[7]))
    e.append(GRAFO.add_edge(v[3],v[4]))
    e.append(GRAFO.add_edge(v[4],v[7]))
    print("PAGE RANK")
    pr = gt.pagerank(GRAFO)
    _pr = list()
    index = 0
    for v in pr:
        _pr.append((index, v))
        index+=1
    del pr
    _pr = sorted(_pr, key=lambda x: -x[1])
    pprint(_pr)
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
    print("CLOSENESS")
    vc = gt.closeness(GRAFO)
    _vc = list()
    index = 0
    for v in vc:
        _vc.append((index,v))
        index+=1
    del vc
    _vc = sorted(_vc,key=lambda x:-x[1])
    pprint(_vc)
    print("EIGENVECTOR")
    evalue, evector = gt.eigenvector(GRAFO)
    _evector = list()
    index = 0
    for v in evector:
        _evector.append((index,v))
        index+=1
    del evector
    _evector = sorted(_evector, key=lambda x:-x[1])
    pprint(_evector)
    print("KATZ")
    kv = gt.katz(GRAFO)
    _kv = list()
    index = 0
    for v in kv:
        _kv.append((index,v))
        index+=1
    del kv
    _kv = sorted(_kv, key=lambda x:-x[1])
    pprint(_kv)
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
    
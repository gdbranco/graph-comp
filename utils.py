import numpy as np

def import_net(file_name):
    """ Import CSV file in the competition format
        Output graph as adjacency list and a set with all nodes """

    print(file_name)
    mt = np.genfromtxt('networks/' + file_name + '.csv',delimiter=',').astype(np.int32)

    # create adjacency list
    network = {}
    for row in mt:
        node1 = row[0]
        node2 = row[1]
        if node1 not in network:
            network[node1] = set()
        if node2 not in network:
            network[node2] = set()
        network[node1].add(node2)
        
    print("All nodes: ", len(network))
    return network

def import_netGT(file_name):
    """ Import CSV file in the competition format
        Output graph as set of edges """
    print(file_name)
    mt = np.genfromtxt('networks/' + file_name + '.csv',delimiter=',').astype(np.int32)
    network = set()
    for row in mt:
        source = row[0]
        target = row[1]
        network.add((source,target))
    return network
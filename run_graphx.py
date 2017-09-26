from graphx import Graph
if __name__ == "__main__":
    g = Graph()
    g.import_net("./networks/real2.csv")
    print(g.V)
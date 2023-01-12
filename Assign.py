class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_List = {}

        for node in self.nodes:
            self.adj_List[node] = []

    def add_edge(self, n1, n2):
        self.adj_List[n1].append(n2)
        self.adj_List[n2].append(n1)

    def remove_edge(self, n1, n2):
        self.adj_List[n1].remove(n2)
        self.adj_List[n2].remove(n1)

    def printNodes(self):
        for node in self.nodes:
            print(node, ":" , self.adj_List[node])




Nodes = ["A", "B", "C", "D", "E"]
graph = Graph(Nodes)
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("B", "E"), ("C", "D"), ("D", "E")]

for a, b in edges:
    graph.add_edge(a, b)

graph.printNodes()

graph.remove_edge("A", "B")
graph.printNodes()
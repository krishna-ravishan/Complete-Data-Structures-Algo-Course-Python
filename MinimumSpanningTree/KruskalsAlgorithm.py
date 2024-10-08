# In kruskals algorithm, it is a greedy algorithm (chooses the best solution available locally)that finds the minimum spanning tree for a connected weighted graph. It does this in two ways.

# 1. Add increasing cost edges at each step
# 2. Avoid any cycle at each step

# Our result must be a tree 

# The pseudo code for kruskal looks like:

# Kruskal(G):
#     for each vertex:
#         nodeSet(v) O(V)
#     sort each edge in non decreasing order by weight O(ElogE)
#     for each edge (u, v): O(E)
#         if findSet(u) != findSet(v):
#             union(u, v) O(V)
#         cost = cost + edge(u, v)

# Time complexity: O(ElogE)
# Space complexity: O(V + E)

# Kruskals Algorithm

import Introduction as dst

class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
        
    def addEdge(self, s, d, v):
        self.graph.append([s, d, v])
        
    def addNode(self, value):
        self.nodes.append(value)
    
    def printSolution(self, s, d, w):
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
            
    def kruskalAlgo(self):
        i = e = 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.printSolution(s, d, w)
        
g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)

g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)

g.addEdge("C", "A", 13)
g.addEdge("C", "E", 20)
g.addEdge("C", "B", 10)
g.addEdge("C", "D", 6)

g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)

g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()
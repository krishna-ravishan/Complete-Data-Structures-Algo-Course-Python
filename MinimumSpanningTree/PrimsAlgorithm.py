# PRIMS ALGORITHM

# It is a greedy algorithm that finds a minimum spanning tree for weighted undirected graphs by first taking any vertex as a source and setting its weight to 0 and all other vertices weight to infinity. Then for every adjacent vertex if the current weight is more than current edge then we set it to current edge adn then we mark the current vertex as visited. It then repeats these steps for all vertices in increasing order of weight.



import sys

class Graph:
    def __init__(self, vertexNum, edges, nodes) -> None:
        self.vertexNum = vertexNum
        self.edges = edges
        self.nodes = nodes
        self.MST = []
        
    def addEdge(self, s, d, v):
        self.graph.append([s, d, v])
        
    def addNode(self, value):
        self.nodes.append(value)
    
    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s - %s: %s" % (s, d, w))
            
    def primsAlgorithm(self):
        visited = [False] * self.vertexNum  # Keep track of visited vertices
        edgeNum = 0  # To count the number of edges in the MST
        visited[0] = True  # Start from the first vertex
        
        while edgeNum < self.vertexNum - 1:
            min_edge = sys.maxsize  # Initialize the minimum edge value to infinity
            s = -1  # Source vertex
            d = -1  # Destination vertex
            
            # Find the minimum edge from the visited vertices to unvisited vertices
            for i in range(self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if not visited[j] and self.edges[i][j]:  # Check if it's a valid edge
                            if self.edges[i][j] < min_edge:
                                min_edge = self.edges[i][j]
                                s = i
                                d = j
            
            if s != -1 and d != -1:  # If a valid edge is found
                self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])  # Add the edge to the MST
                visited[d] = True  # Mark the destination vertex as visited
                edgeNum += 1  # Increment the edge count
        
        self.printSolution()  # Print the MST when finished
        

# Adjacency matrix representation of the graph
edges = [
    [0, 10, 20, 0, 0],
    [10, 0, 30, 5, 0],
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0],
]
nodes = ["A", "B", "C", "D", "E"]

# Create a graph instance and run Prim's Algorithm
g = Graph(5, edges, nodes)
g.primsAlgorithm()

# Time complexity : O(V^3) or O(ELogV) with adjacency list
# Space Complexity: O(V)

# Differences between Prims & Kruskals Algorithm

# Kruskals focuses on edges, and finalized edges in each iteration.
# Applications are landing cables tv networks tour operations lan networks electric grid etc.

# Prims algo focuses on vertices and finalizing vertex with each iteration
# Applications are network for road and rail tracks, irrigation channels, designing fiber optic grid traveling salesman problem
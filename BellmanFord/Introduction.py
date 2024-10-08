# Bellman ford Algorithm

# It is used to find single source shortest path problem. If there is a negative cycle in graph it catches it and reports its existence. We cannot find the shortest path when there is a negative cycle.

# If the distance of a destination vertex > (dist of src vetex + weight btwn src and dest vertex) then update the distance to dist of src vetex + weight btwn src and dest vertex.

# Bellman ford uses DP and Dijkstra uses greedy approach. Bellman is slower but can handle negative weights by relaxing it. 

# In bellman ford we've to do iterations V-1 times. On Vth iteration the algorithm can identify whether the graph has a negative cycle or not.

# Why V-1? It tries to see if any node has achieved better distance in previous iteration, then that better distance is used to improve the distance of other vertices. We can identify worst case graph can be given to us. It has to be the number of edges between connected graph of worst case scenario therefore it runs v-1 times.

# Implementation

class Graph:

    def __init__(self, vertices):
        self.V = vertices   
        self.graph = []     
        self.nodes = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def addNode(self,value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for key, value in dist.items():
            print('  ' + key, ' :    ', value)
    
    def bellmanFord(self, src):
        dist = {i : float("Inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V-1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative cycle")
                return
        

        self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")

# Time complexity: O(VE)
# Space complexity: O(V)

# BFS vs Dijkstra vs Bellman Ford

# Time complexity for BFS and dijstra is O(V^2) and bellman ford is O(VE)
# BFS does not work for weighted graphs, does not work for negative cycles. Bellman ford works for all.
# Use BFS for unweighted graph as time complexity is good and it is easy to implement
# Use Dijkstra when it is weighted graph as tc is better than bellman ford
# Use bellman when there is negative cycle
# Dijkstra's Algorithm
# This works for weighted graphs

# First assume that the distance to all nodes is infinity and the cost of node from itself (starting node) is 0.
# Now we'll continue with the neighboring node that has minimum cost.
# It can work for directed and non directed graphs as well.

# We're going to be using the heap data structure because its easy to rearrange the heap data structure in logN time complexity.
import heapq

class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.min_distance = float("inf")
        
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)
            
class Dijkstra:
    def __init__(self):
        self.heap = []
        
    def calculate(self, starting_vertex):
        starting_vertex.min_distance = 0
        heapq.heappush(self.heap, starting_vertex)            
        while self.heap:
            # Pop element with lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # Consider neighbors 
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = actual_vertex.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start 
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True
                
    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
        

print(Edge(10, 'A', 'B').weight)

# Step 1: Creating Nodes

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

# Step 2: Creating Edge

nodeA.add_edge(6, nodeB)
nodeA.add_edge(10, nodeC)
nodeA.add_edge(9, nodeD)

nodeB.add_edge(5, nodeD)
nodeB.add_edge(13, nodeF)
nodeB.add_edge(16, nodeE)

nodeC.add_edge(5, nodeH)
nodeC.add_edge(21, nodeG)
nodeC.add_edge(6, nodeD)

nodeD.add_edge(8, nodeF)
nodeD.add_edge(7, nodeH)

nodeE.add_edge(10, nodeG)

nodeF.add_edge(4, nodeE)
nodeF.add_edge(12, nodeG)

nodeH.add_edge(2, nodeF)
nodeH.add_edge(14, nodeG)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.get_shortest_path(nodeF)

# Dijkstra's algorithm with Negative Cycles (If negative weight in cycle and total weight of cycle is negative)

# If negative cycle then dijkstra cannot recognize it and does not stop therefore we cannot use it.





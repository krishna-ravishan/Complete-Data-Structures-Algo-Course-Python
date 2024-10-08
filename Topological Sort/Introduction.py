# Topological Sort

# In topological sort, sort is given actions in such a way that if there is a dependency of a one action on another, then the dependent action always comes later than its parent action.

# Real Life example: Take your morning routine, first excercise, bath, breakfast, work. But we cannot have a bath without exercise and we cannot have breakfast without buying breakfast ingredients and preparing breakfast.

# Say we have a directed graph consisting of 8 vertices. A B C D E F G H

# Algorithm (Using stack data structure)

# if a vertex depends on currentVertex:
#   Go to that vertex and then come back to current vertex
# else
#   Push currentVertex to stack

# Time Complexity: O(V + E)
# Space Complexity: O(V)

# Graph Class
from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # Helper function
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        # Recursively call this function for all adjacent vertices of the current vertex
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)
    
    def topologicalSort(self):
        visited = []
        stack = []
        for j in list(self.graph):
            if j not in visited:
                self.topologicalSortUtil(j, visited, stack)
        print(stack)

customGraph = Graph(8)
customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")
customGraph.topologicalSort()

# GRAPHS
# What is graph?
# It's a non linear data structure that consists of a finite set of vertices and a finite set of edges.

# Why is it needed?
# Used to represent networks in real life.
# Used in google maps, railway tracks etc.
# Can consists of cycles

# Graph Terminology
# Vertices (Vertex): These are the nodes of graph
# Edge: An edge is the line that connects pairs of vertices
# Unweighted graph: A graph which has a weight associated with any edge
# Weighted graphs: A graph which has a weight associated with every or any edge
# Undirected Graph: In case edges do not have a direction associated with them
# Directed Graph: If edges in a graph have a direction associated with them.
# Cyclic Graph: A Graph which has at least one loop is called a cyclic graph
# Acyclic Graph: A Graph which does not have any loops is called a cyclic graph# Tree
# Tree: A special case of directed acyclic graph

# Different Types of Graphs

# 1. Unweighted UnDirected Graph
# Can travel in any direction therefore undirected and no weights associated with the edges

# 2. Unweighted Directed
# Can travel only in the direction pointed by the edges(arrows). But no weights associated with edges

#  Similarly positive and negative and others

# GRAPH REPRESENTATION

# We use an adjacency matrix. A matrix is a square matrix or you can say it is a 2D array. And elements of a matrix indicate whether pairs of vertices are adjacent or not in the graph

# Draw out a N X N Map for all vertices and initialize all to zero. Then if there is connection update it to 1.

# An adjacency list can be used as well. Each list describes the set of neighbors of a vertex in a graph

# If space is few then use matrix else list
# Cannot reduce number of vertexes in matrix

# We can have python dictionary representation as well.

# graph = {
#     A: [B, C, E],
#     B: [A, D],
#     C: [D, A, E],
#     D: [B, C, E],
#     E: [A, D]
# }

# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)

#     def addVertex(self, vertex, edges_list):
#         self.gdict[vertex] = edges_list

from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def addEdge(self, vertex, edge):
        if edge not in self.adjacency_list.keys() and vertex not in self.adjacency_list.keys():
            return "Edge vertex is not in graph"
        self.adjacency_list[vertex].append(edge)
        self.adjacency_list[edge].append(vertex)
        return True
    
    def removeEdge(self, vertex, edge):
        if vertex in self.adjacency_list.keys() and edge in self.adjacency_list.keys():
            self.adjacency_list[vertex].remove(edge)
            self.adjacency_list[edge].remove(vertex)
            return True
        return False
    
    def removeVertex(self, vertex):
        # if vertex in self.adjacency_list.keys():
        #     del self.adjacency_list[vertex]
        #     return True
        # return False
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
        print("")

    # For dfs we're going to use a stack
    def dfs(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex, end=" ")
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
        print("")






customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f", "c"],
    "f": ["d", "e"]
}

graph = Graph()
print(graph.adjacency_list)
graph.addVertex("C")
graph.addVertex("D")
print(graph.adjacency_list)
graph.print_graph()
graph.addEdge("C", "D")
graph.print_graph()
graph.bfs("C")
graph.removeEdge("C", "D")
graph.print_graph()
graph.removeVertex("C")
graph.print_graph()

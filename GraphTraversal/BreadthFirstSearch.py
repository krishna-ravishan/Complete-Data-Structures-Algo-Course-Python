# Introduction
# The process of visiting each node is called the traversal of graph
# Graph can be traversed in two ways:
# 1. Breadth First Search
# 2. Depth First Search

# BREADTH FIRST SEARCH: In bfs we basically traverse all the neighbouring nodes of the vertex and then process further until all nodes are visited

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D'],
    'C': ['D', 'A', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['A', 'D']
}


def bfs(self, vertex):
    visited = set()
    visited.add(vertex)
    queue = [vertex]
    while queue: # O(V)
        current_vertex = queue.pop(0)
        print(current_vertex, end=" ")
        for adjacent_vertex in self.adjacency_list[current_vertex]: # O(E)
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)
                queue.append(adjacent_vertex)

# The Time complexity for breadth first search is O( V + E )
# This is because each vertex and edge only one time.
# The Space complexity for breadth first search is O(V) 
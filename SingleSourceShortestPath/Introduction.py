# A SSSP problem is about finding a path between a given vertex to all other vertices in a graph such that the total distance between them is minimum.

# The problem:

# 1. Five offices in different cities
# 1. Travel cost between these cities are known
# 3. Find the cheapest way from head office to branches in different cities

# 1. BFS
# 2. Dijkstra's algorithm
# 3. Bellman Ford Algorithm

# BFS For Single Source Shortest Path

# enqueue any starting vertex 
# while queue is not empty
# p = dequeue()
# if p is unvisited mark p as visited, enqueue all adjacent unvisited vertices of p then update parent of adjacent vertices to curVertex

# Time Complexity for BFS: O(E) This is because in SSSP problem we're only traversing the connected vertices. SO if there are any isolated vertices we wont visit it.
# Space Complexity for BFS: O()
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


customDict = {
    'A': ['B', 'C'],
    'B': ['D', 'G'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'G': ['F']
}

g = Graph(customDict)
print(g.bfs("A", "E"))

# The problem is that bfs for SSSP problems doesn't not work with weighted graphs.
# Similarly, DFS has a tendency to go to the deepest and furthest node first and therefore does not work for SSSP problems.


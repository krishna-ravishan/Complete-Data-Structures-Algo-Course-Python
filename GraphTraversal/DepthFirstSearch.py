# Depth First Search
# DFS is an algorithm used for traversing or searching through data structures like graphs and trees. In depth first search, we explore as far down a branch or connected vertices as possible before back tracking. You explore as deeply as possible along each branch before moving to the next branch.

# DFS uses a stack

# The Time complexity for DFS is O(V + E) Since we're visiting each vertex and edge once.
# Space complexity is O(V)


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

# The difference between depth first search and breadth first search

# How does it work internally: Breadth | Depth
# Which DS does it use internally: Queue | Stack
# Time Complexity: It is the same
# Space Complexity: It is the same
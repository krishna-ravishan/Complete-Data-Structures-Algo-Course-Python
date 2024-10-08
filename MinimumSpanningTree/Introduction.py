# Minimum Spanning Tree

# By definition a minimum spanning tree is a subset of the edges of connected, weighted and undirected graphs which connects all vertices together, has no cycle and gives minimal total cost of edges

# A real life examples of this is connect 5 islands with bridges

# This is not the same as single source shortest path as we're not choosing a vertex/source and the minimum distance from that vertex to all others.

# Disjoint set: We'll be using this inside algorithm of minimum spanning tree. It is a data structure that keeps track of set of elements which are partitioned into a number of disjoint and non overlapping sets and each sets have representative which helps in identifying that sets.

# Three standard operations. 1. Makeset 2. Union 3. Find Set

# 1. Make Set: Used to create set for n number of elements.

# 2. Union: Used to merge two given sets.

# 3. Find Set: returns the set name in which this element is there. 

# Creating disjoint set in python


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
    
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
            
            
# vertices = ["a", "b", "c", "d", "e"]

# ds = DisjointSet(vertices)
# ds.union("a", "b")
# print(ds.find("b"))
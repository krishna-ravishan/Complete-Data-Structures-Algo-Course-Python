import heapq

"""
Each task is
T1 - 5
T2 - 4
T3 - 7
T4 - 9
T5 - 2
T6 - 6

A heap is an implementation of a priority queue using a binary tree data structure. 
If child index is i then parent is i/2 - 1 

What should be the size of the array?
in worst case all levels of tree will be filled and be a perfect bianry tree so the number of nodes wil by 2^(h+1) - 1 where h is height of tree starting from 0.
Height of tree = log2N for n number of nodes given.

Range of leaves = n/2 + 1
Heapify Algorithm
# If heap size is N then range of leaves will range form n/2 to n - 1.

Heap Property. if max heap then root node should be greater than all left and right subtree nodes and recursively true for all subtrees. if min heap then root node should be lesser than all left and right subtree nodes and recursively true for all subtrees.

The process of rearranging the heap by comparing each parent with its child recursively is known as heapify.

Build heap algorithm: Heapify all internal nodes. 
"""

data = [3,2,1,5,6,4]
heapq.heapify(data)
print(data)

print(heapq.heappop(data))
print(data)
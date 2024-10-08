"""
BINARY HEAP

A binary heap is a binary tree with additional properties.

1. A binary heap is either min heap or max heap. In min heap, the key at root must be minimum among all keys present in binary heap. The same property must be recursively true for all nodes in binary tree. In max binary heap, the key at root node must be maximum among all keys present in binary tree

2. It's a complete tree (All levels are completely filled except for the last level and the last level has all keys as left as possible). The property of binary heap makes them suitable to be stores in an array.

Why do we need a binary heap?

Find the minimum or maximum number among a set of numbers in logN time. And also we want to make sure that inserting additional numbers does not take more than O(logN) time.

Practical Use of binary heap
1. Prims Algorithm
2. Heap Sort
3. Priority Queue

Types of binary heap: 1. Min Heap: The value of each node is less than or equal to the value of both of its children. 
2. Max Heap: It's exactly the opposite of min heap that is the value of each node is more than or equal to the value of both its children.

Common operations on a Binary Heap
1. Creation
2. Peek Top
3. Extract Min/Max
4. Traversal
5. Size of binary heap
6. Inserting/Deleting element in binary heap

It is best to use the list implementation of binary heap similar to binary tree
Left Child: cell[2x]
Right Child: cell[2x + 1]

Creation of binary heap: initial fixed size list, set size of binary heap to 0.
Takes O(1) time complexity to declare binary heap
Peak of Heap: Return root of heap

"""

class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Peek operation takes O(1) time complexity and space complexity
def peekOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]
# Size of binary heap takes O(1) time complexity and space complexity
def sizeOfHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

# Level Order Traversal has a time complexity of O(N) and space complexity is O(1)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i], end=" ")

# Binary Heap should be complete binary tree
# Inserting a node into binary heap. Time complexity for extracting node is O(LogN). Similarly SC = O(LogN)


def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[index]
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The binary tree is full"
    rootNode.customList[rootNode.heapSize + 1] =  nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

# Extract an element from binary heap. Heap does not allow any other node value to be extracted other than that of the root node because this is the property of heap
def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    # Check if node has children or not
    if rootNode.heapSize < leftIndex:
        return
    # If only one node for root node and it is left child
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]      
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                rootNode.customList[index], rootNode.customList[leftIndex] = rootNode.customList[leftIndex], rootNode.customList[index]      
            return
    else:
        if heapType == "Min":
            if rootNode.customList[rightIndex] > rootNode.customList[leftIndex]:
                swapChild = leftIndex      
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]      
        elif heapType == "Max":
            if rootNode.customList[rightIndex] < rootNode.customList[leftIndex]:
                swapChild = leftIndex      
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                rootNode.customList[index], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[index]      
        heapifyTreeExtract(rootNode, swapChild, heapType)

# Time complexity for extracting node is O(LogN). Similarly SC = O(LogN)
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    extractedNode = rootNode.customList[1]
    rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize] = None
    rootNode.heapSize -= 1
    heapifyTreeExtract(rootNode, 1, heapType)
    return extractedNode

# O(1) Time complexity and Space Complexity
def deleteHeap(rootNode):
    rootNode.customList = None

newHeap = Heap(10)
print(insertNode(newHeap, 4, "Max"))
print(insertNode(newHeap, 9, "Max"))
print(insertNode(newHeap, 7, "Max"))
print(insertNode(newHeap, 1, "Max"))
levelOrderTraversal(newHeap)
print()
print(extractNode(newHeap, "Max"))
levelOrderTraversal(newHeap)
deleteHeap(newHeap)
levelOrderTraversal(newHeap)


        



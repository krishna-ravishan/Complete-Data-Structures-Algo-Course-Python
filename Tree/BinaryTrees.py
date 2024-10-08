# BINARY TREES
# Binary trees are data structures in which each node has at most two children, often referred to as left and right children

# Not possible to have more than two data structures

# Why binary trees?
# 1. Prerequisite for more advanced trees like BST, AVL, Red Black Trees
# 2. Huffman coding problem, heap priority etc can be solved with binary trees

# Types of binary Trees
# 1. Full Binary Tree - Each node has either 0 or 2 children
# 2. Perfect Binary Tree - Each node has two children and all leaf nodes are located on the same level
# 3. Complete Binary Tree - Each node has two children but not necessary that all leaf nodes are on the same level. Must follow from left to right convention
# 4. Balanced Binary Tree - Each leaf node is not more than a certain distance from the root node

# Let's Create a Binary Tree
# There are two ways. 1. Linked List 2. Python List (Array)

# In List
# Left Child = cell(2x)
# Right Child = cell(2x + 1)

#   0     1        2      3      4     ...... & So on
#   x   Drinks    Hot    Cold   Tea

# Traversal of Binary Tree
# There are 4 types: 
# DEPTH FIRST SEARCH
# 1. Preorder Traversal
# 2. Inorder Traversal
# 3. Post order Traversal
# BREADTH FIRST SEARCH
# 1. Level Order Traversal

# A1. Pre-order Traversal (Root Node -> Left Subtree -> Right Subtree) (Similar to depth first search)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# A2. Inorder Traversal (Left Subnode -> Root Node -> Right Subnode)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# A3. Post Order Traversal (Left Subnode -> Right Subnode -> Root Node)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# B1. Level Order Traversal (We visit tree level by level)
from collections import deque

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while len(customQueue) > 0:
            root = customQueue.popleft()
            print(root.data)
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            if root.rightChild is not None:
                customQueue.append(root.rightChild)


def searchTree(rootNode, target):
    if not rootNode:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while len(customQueue) > 0:
            root = customQueue.popleft()
            if root.data == target:
                return True
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            if root.rightChild is not None:
                customQueue.append(root.rightChild)
    return False

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while len(customQueue) > 0:
            node = customQueue.popleft()
            if node.leftChild is not None:
                customQueue.append(node.leftChild)
            else:
                node.leftChild = newNode
                return 'Successfully inserted'
            if node.rightChild is not None:
                customQueue.append(node.rightChild)
            elif node.leftChild is not None:
                node.rightChild = newNode
                return 'Successfully inserted'

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while customQueue:
            root = customQueue.popleft()
            if root.leftChild is not None:
                customQueue.append(root.leftChild)
            if root.rightChild is not None:
                customQueue.append(root.rightChild)
            deepestNode = root.value
        return deepestNode


def delete_node(rootNode, target):
    if not rootNode:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while customQueue:
            node = customQueue.popleft()
            if node.data == target:
                node.data = None
            if node.rightChild:
                if node.rightChild is target:
                    pass

def delete_tree(rootNode):
    rootNode = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Binary Tree Deleted Successfully"


preOrderTraversal(newBT)
# inOrderTraversal(newBT)
# postOrderTraversal(newBT)
# print(levelOrderTraversal(newBT))
# print(searchTree(newBT, "Hot"))
new_node = TreeNode('Mild')
new_node_2 = TreeNode('Extreme')
print(insertNode(newBT, new_node))
print(insertNode(newBT, new_node_2))
print(insertNode(newBT, new_node))
print(insertNode(newBT, new_node_2))
preOrderTraversal(newBT)



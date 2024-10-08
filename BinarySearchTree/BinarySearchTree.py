# What is a binary search tree?
# In the right subtree the value of a node is greater than or equal to its parent node value
# In the left subtree the value of a node is than or equal to its parent node value

# It performs faster than binary tree when inserting and deleting nodes.

class BSTNode():
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# O(LogN) Time Complexity
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully been inserted!"
    
# Traversal for Binary Search Tree

# Preorder Traversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Inorder Traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Post Order Traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Level Order Traversal
from collections import deque

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = deque()
        customQueue.append(rootNode)
        while customQueue:
            node = customQueue.popleft()
            print(node.data)
            if node.leftChild is not None:
                customQueue.append(node.leftChild)
            if node.rightChild is not None:
                customQueue.append(node.rightChild)
            
def search(rootNode, target):
    # if not rootNode:
    #     return
    # else:
    #     customQueue = deque()
    #     customQueue.append(rootNode)
    #     while customQueue:
    #         node = customQueue.popleft()
    #         if node.data == target:
    #             return True
    #         if node.leftChild is not None:
    #             customQueue.append(node.leftChild)
    #         if node.rightChild is not None:
    #             customQueue.append(node.rightChild)
    #     return False
    try:
        if rootNode.data == nodeValue:
            print("The value is found")
        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild.data == nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.rightChild, nodeValue)
    except:
        print("The value is not found")
        return False

# Three cases, Node is leaf node, node has one child and node has two children. In last case, we need to find successor of node which will be the smallest node in the right subtree.

def minValue(rootNode):
    current = rootNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def delete(rootNode, target):
    if not rootNode:
        return
    if target < rootNode.data:
        rootNode.leftChild = delete(rootNode.leftChild)
    elif target > rootNode.data:
        rootNode.rightChild = delete(rootNode.rightChild)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = delete(rootNode.rightChild, temp.data)
        return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return True

newBST = BSTNode(None)
print(insertNode(newBST, 10))
print(insertNode(newBST, 0))
print(insertNode(newBST, 20))
# print(newBST.rightChild.data)
# preOrderTraversal(newBST)
inOrderTraversal(newBST)
# levelOrderTraversal(newBST)
print(search(newBST, 30))
print(delete(newBST, 10))
inOrderTraversal(newBST)

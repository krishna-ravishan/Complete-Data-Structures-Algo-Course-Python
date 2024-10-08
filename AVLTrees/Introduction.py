# AVL Trees

# An AVL Tree is a self balancing binary search tree where the difference between the heights of the left and right subtrees cannot be more than one for all nodes.

# Why AVL Trees

# Allows us to conduct faster search, insert and delete operations. For balanced tree, the time complexity you have is O(LogN) and for unbalanced tree in worst case scenario it can reach to O(N)

# Common Operations on AVL Trees

# Creation of AVL Trees - Same as binary tree
# Search for a node - Preorder, Inorder, postorder traversal, level order traversal.
# Traverse all nodes
# Insert a node
# Delete a node 
# Delete entire AVL Tree

class AVLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1
        
# Same as normal BST
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

# There can be two cases: 1. Rotation is not required 2. Rotation is required.
# First find the unbalanced node
# LL Condition - Left Left condition we have to do right rotation. First the rightChild of the leftchild of the unbalanced node becomes the leftchild of the unbalanced node.

# Algorithm looks like:
# rotateRight(unbalancedNode):
#     newRoot = unbalancedNode.leftChild
#     unbalancedNode.leftChild = unbalancedNode.leftChild.rightChild
#     newNode.rightChild = unbalancedNode
#     update hegiht of disbalanced node and newRoot
#     return newRoot

# LR Condition - Left Right condition we have to do right rotation. LEft rotation and then right rotation. First the rightChild of the leftchild of the unbalanced node becomes the leftchild of the leftchild of the unbalanced node. Then we have LL condition so we've to do right rotation. 

# Step 1: Rotate left the disbalancedNode.leftChild
# Step 2: Rotate Right the disbalancedNode

# Algorithm looks like:
# rotateLeft(unbalancedNode):
#     newNode = unbalancedNode.rightChild
#     unbalancedNode.rightChild = unbalancedNode.rightChild.leftChild
#     newNode.leftChild = unbalancedNode
#     update height of disbalanced node and newRoot
#     return newRoot

# RR condition. _ One time rotate left

# RL Condition. _ One time rotate right then left

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue == rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)    
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    # LL
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rotateRight(rootNode)
    # LR
    if balance > 1 and nodeValue > rootNode.leftchild.data:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return rotateLeft(rootNode)
    if balance < -1 and nodeValue < rootNode.leftchild.data:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode 

# Case 1 - Rotation is not required
# Subcase 1.1: The node to be deleted is a leaf node.
# Subcase 1.2: The node to be deleted is a node with 1 child.
# Subcase 1.3: The node to be deleted is a node with 2 children. Here we've find the successor of this node.

# Case 2 - Rotation is required - First delete node, then balance
# Subcase 1: LL 
# Subcase 2: LR
# Subcase 3: RR
# Subcase 4: RL

# 

def getMinValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValue(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        elif rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        temp = getMinValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    # LL
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rotateRight(rootNode)
    # LR
    if balance > 1 and getBalance(rootNode.rightChild) < 0:
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode)
    # RR
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return rotateLeft(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) >= 0:
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    return rootNode
    
   
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rotateRight(unbalancedNode):
    newRoot = unbalancedNode.leftChild
    unbalancedNode.leftChild = unbalancedNode.leftChild.rightChild
    newRoot.rightChild = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.leftChild), getHeight(unbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def rotateLeft(unbalancedNode):
    newRoot = unbalancedNode.rightChild
    unbalancedNode.rightChild = unbalancedNode.rightChild.leftChild
    newRoot.leftChild = unbalancedNode
    unbalancedNode.height = 1 + max(getHeight(unbalancedNode.leftChild), getHeight(unbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

newAVL = AVLNode(5)
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
levelOrderTraversal(newAVL)
deleteNode(newAVL, 10)
levelOrderTraversal(newAVL)

def deleteTree(rootNode):
    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode = None
    return "Successfully deleted"
    
print(deleteTree(newAVL))
levelOrderTraversal(newAVL)

# Time complexity is O(LogN)
# Space complexity is O(logN)
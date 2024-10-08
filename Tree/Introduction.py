# A tree is a non linear data structure with hierarchial relationships between its elements without having any cycle.

# Real life examples: You want to order drinks then you have two options, hot and cold. under hot you have tea and coffee and in cold you have non alcoholic and alcoholic and so on and so forth

# Represent hierarchial data structures
# Each node has two components: Data and a link to its sub category
# Each base category has sub categories under it unless its leaf node

# Why a tree?
# It is a non linear data structure
# quicker and easier access to data
# Store data in a hierarchy. For example the file system.
# There are different types of data structures which perform better in various situations
# -- BST, AVL, Red Black Tree, Trie (Prefix Tree)

# Tree Terminologies

# Root: Top node without parent.
# Edge: A link between parent and child
# leaf: A node without children 
# Child: Sub-Node of a Parent Node
# Siblings: Children of same parents
# Ancestor: Parent, GrandParent, Great Great Grandparent
# Depth of Node: (Starts from 0) Can out number of nodes - 1 or simply the number of edges from root node to node
# Height of a Node: A Length of the path from node to deepest node
# Depth of Tree: Depth of root node. (Always 0)
# Height of Tree: Height of root node. Can out number of nodes - 1 or simply the number of edges from root node to node 

# BASIC TREE

class TreeNode():
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = ("  " * level) + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
            # print(ret)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)
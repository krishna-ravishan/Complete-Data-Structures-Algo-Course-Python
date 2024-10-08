# Left Child: cell[2x]
# Right Child: cell[2x + 1]

class BinaryTree():
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def __str__(self):
        res = ''
        for i in range(self.lastUsedIndex + 1):
            res += str(self.customList[i])
            res += " "
        return res
    
    # Insert Node to Binary Tree
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Binary Tree is Full"
        else:
            self.customList[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1
            return "Value inserted successfully"

newBT = BinaryTree(8)
print(newBT)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
print(newBT.insertNode("Cold"))
print(newBT)
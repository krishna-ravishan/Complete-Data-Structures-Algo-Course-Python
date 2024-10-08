# Describe how you'll use a single python list to implement three stacks

#  Imagine you've a list, you simply divide it into three parts. The first stack will contain top1, second stack will contain top 2 and third stack will contain top 3

# For stack 1 - [0][1][2]
# For stack 2 - [3][4][5]
# For stack 3 - [6][7][8]

class Stack:
    def __init__(self, stackSize):
        self.numberstacks = 3
        self.stackSize = stackSize
        self.custList = [0] * (stackSize * self.numberstacks)
        self.sizes = [0] * self.numberstacks

    def isFull(self, stacknum):
        if self.sizes[stacknum] == self.stackSize:
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexofTop(self, stacknum):
        offset = stacknum * self.stackSize
        return offset + self.sizes[stacknum] - 1
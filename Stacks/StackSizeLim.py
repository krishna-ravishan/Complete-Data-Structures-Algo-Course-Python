class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # isEmpty Method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # isFull Method
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    # push Method
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)
            return "The element has been pushed successfully"
        
    # pop Method
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()
    
    # peek Method
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[-1]
    
    # delete Method
    def delete(self):
        self.list = None

newStack = Stack(4)
print(newStack)
print(newStack.push(10))
print(newStack.push(20))
print(newStack.push(30))
print(newStack.push(40))
print(newStack.push(50))
print(newStack)
print(newStack.isEmpty())
print(newStack.pop())
print(newStack.peek())
# Implement a stack using a queue

# class Stack:
#     def __init__(self):
#         self.list = []

#     def __str__(self):
#         return str(self.list)
    
#     def push(self, value):
#         self.list.append(value)

#     def pop(self):
#         return self.list.pop()
    
class QueueviaStack():
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def enqueue(self, value):
        self.inStack.append(value)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.append(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.append(self.outStack.pop())
        return result
    
customQueue = QueueviaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
# class Queue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.list = []
#         self.start = -1
#         self.top = -1

#     def __str__(self):
#         values = [str(x) for x in self.list]
#         return " ".join(values)

#     def isEmpty(self):
#         if len(self.list) == 0:
#             return True
#         else:
#             return False
    
#     def isFull(self):
#         if len(self.list) == self.capacity:
#             return True
#         else:
#             return False

#     def enqueue(self, value):
#         if self.isFull():
#             return "Queue is full"
#         else:
#             self.list.append(value)
#             if self.isEmpty():
#                 self.start += 1
#             self.top += 1
#             return "Enqueue Successful"
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "Queue is Empty"
#         else:
#             self.list.pop(0)
#             self.start += 1
#             return "dequeue Successful"
    
#     def peek(self):
#         return self.list[start]

#     def deleteQueue(self):
#         self.list = None

# Circular Queue

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if -1 == self.top:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if self.isFull():
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return 'The element is inserted at the end of the queue'
        
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.items = self.maxSize * [None]
        self.top -= 1
        self.start -= 1

newQueue = Queue(4)
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
newQueue.dequeue()
print(newQueue.isEmpty())
print(newQueue)
        
    

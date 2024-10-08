# A Queue is a data structure that stores data in a First In First Out (FIFO) Manner.

# A new addition happens at the end of the queue and removal happens at the beginning of the queue.

# There is a front and an end of the queue. An element is added at the end of the queue and removed or taken from the queue

# Serving system for a restaurant or printer queue

# Queue Operations
# 1. Create Queue
# 2. Enqueue
# 3. Dequeue
# 4. Peek
# 5. isEmpty
# 6. isFull
# 7. deleteQueue

# Can be implemented with lists and linked lists. We have two types in lists type queue. Queue with and without capacity

class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue(self, value):
        self.list.append(value)
        return "Enqueue Successful"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.list.pop(0)
            return "dequeue Successful"
        
    def deleteQueue(self):
        self.list = None


newQueue = Queue()
newQueue.enqueue(10)
newQueue.enqueue(20)
newQueue.enqueue(30)
newQueue.enqueue(40)
print(newQueue)
newQueue.dequeue()
print(newQueue)

            
                
# The collections.deque class

# from collections import deque

# # Methods
# # deque()
# # append()
# # popleft()
# # clear()

# customQueue = deque(maxlen=3)
# print(customQueue)
# customQueue.append(1)
# customQueue.append(2)
# customQueue.append(3)
# customQueue.append(4) # Overwrites the first element from queue
# print(customQueue)
# customQueue.popleft()
# print(customQueue)
# customQueue.clear()
# print(customQueue)

# The Queue Model

# LIFO Queue is a stack

# import queue as q

# customQueue = q.Queue(maxsize=3)
# print(customQueue)
# print(customQueue.empty())
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)
# print(customQueue.qsize())
# print(customQueue.full())

# The multiprocessing module

from multiprocessing import Queue

customQueue = Queue(maxsize=3)
print(customQueue)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue)

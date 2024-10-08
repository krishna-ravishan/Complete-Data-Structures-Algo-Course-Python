class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __str__(self):
#         temp = self.head
#         res = []
#         while temp:
#             res.append(str(temp.value))
#             temp = temp.next
#         return "\n".join(reversed(res))
    
#     def push(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return "Inserted element successfully"
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             return "Inserted element successfully"

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None

newStack = Stack()
newStack.push(10)
newStack.push(20)
newStack.push(30)
print(newStack)
print(newStack.isEmpty())
print(newStack.pop())
print(newStack.peek())
print(newStack)
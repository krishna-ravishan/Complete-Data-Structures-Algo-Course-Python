# Stack is a Last in First Out (LIFO) data structure.
# Imagine a stack of plates. In order to take one plate from the stack you need to take the last plate first. 

# We need a stack data structure whenever we have an application that requires the last event to be the first to occur. 

# Eg the back button on chrome.

# There are a few stack operations 
# 1. Create Stack
# 2. Push - insert element to top of stack
# 3. Pop - delete element from top of stack
# 4. Peek - return element at the top
# 5. isEmpty - return True if stack is empty
# 6. isFull - return True if stack is full
# 7. deleteStack - delete stack elements

# Stack Creation 

# We can implement a stack using a list or linked list. Using list, its easy to implement but you have memory allocation problems when the stack grows which is time consuming. Using linked list it performs fast but the implementation is not easy.

# Implementation of Stack using List

class Stack:
    def __init__(self):
        self.list = []

    # def __str__(self):
    #     values = self.list.reverse()
    #     values = [str(x) for x in self.list]
    #     return '/n'.join(values)
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # isEmpty Method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # push Method
    def push(self, value):
        self.list.append(value)
        return "The element has been pushed successfully"
    
    # pop Method
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
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

newStack = Stack()
print(newStack.push(10))
print(newStack.push(20))
print(newStack.push(30))
print(newStack)
print(newStack.isEmpty())
print(newStack.pop())
print(newStack.peek())
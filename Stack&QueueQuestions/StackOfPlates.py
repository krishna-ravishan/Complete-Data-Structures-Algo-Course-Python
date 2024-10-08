class DinnerPlates:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)
    
    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            popped_element = self.stacks[-1].pop()
            return popped_element
        
    def popAtStack(self, index):
        if len(self.stacks[index]) >= 0:
            popped = self.stacks[index].pop()
            return popped
        else:
            None

newStack = DinnerPlates(2)
newStack.push(1)
newStack.push(2)
newStack.push(3)
print(newStack)
newStack.pop()
print(newStack)
newStack.pop()
print(newStack)
newStack.popAtStack(0)
print(newStack)

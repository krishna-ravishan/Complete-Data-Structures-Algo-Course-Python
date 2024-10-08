class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        # return f"{self.prev} <-{self.value}->{self.next}"
        return str(self.value)
    
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        res = ''
        for _ in range(self.length):
            res += str(temp.value)
            if temp.next is not None:
                res += ' <-> '
            temp = temp.next
        return res

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value, end=' ')
            curr = curr.next
    
    def search(self, target):
        curr = self.head
        index = 0
        while curr:
            if target == curr.value:
                return (True, index)
            index += 1
            curr = curr.next
        return False

    def reverse_traverse(self):
        curr = self.tail
        while curr:
            print(curr.value, end=" ")
            curr = curr.prev

    def get(self, index):
        if index < self.length // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.length -1, index, -1):
                curr = curr.prev
        return curr

    def set(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node

    def popFirst(self):        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            popped_node.prev = None
            self.tail.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node
    
newDoubly = DoublyLinkedList()
newDoubly.append(10)
newDoubly.append(20)
newDoubly.append(30)
newDoubly.prepend(0)
print(newDoubly)
print(newDoubly.search(10))
print(newDoubly.get(0))
print(newDoubly.reverse_traverse())


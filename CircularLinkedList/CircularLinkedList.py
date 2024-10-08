class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
 
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " --> " 
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node      
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        temp = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = temp
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length + 1:
            # self.append(value)
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head                
        else:
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def traverse(self):
        if self.head is None:
            return None
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next

    def search(self, target):
        temp = self.head
        while temp is not None:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def get(self, index):
        if index < -1 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def set(self, index, value):
        if index < -1 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        if temp:
            temp.value = value
            return True
        return False
    
    def PopFirst(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail == None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.tail.next = self.head
        self.length -= 1
        return temp

    def Pop(self):
        temp = prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = self.head
        temp.next = None
        self.length -= 1
        return temp
    

csll = CSLinkedList()
csll.append(10)
csll.append(20)
csll.append(30)
csll.prepend(0)
csll.insert(70, 4) 
csll.traverse() 
print(csll.search(40))
print(csll)
print(csll.get(2))

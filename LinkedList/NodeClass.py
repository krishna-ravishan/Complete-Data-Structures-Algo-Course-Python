# A node is composed of the value of the node and the address of the next node

# We are going to create a separate class for a node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# new_node = Node(10)
# print(new_node)

# Creation of a Singly Linked List

# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


# EMPTY LINKED LIST
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

# In order to insert a node in the beginning of a SLL, add the address of the first node to the new node and point the header from the first node to the new node. For insertion of a node after a node (in the middle) you have to get the new node to point where the old node is pointing at and then reference the old node next pointer to the new node.

# INSERT NODE AT THE END OF THE LINKED LIST - (Append a node)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
    
#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

# new_linked_list = LinkedList()
# print(new_linked_list.length)
# new_linked_list.append(30)
# new_linked_list.append(20)
# new_linked_list.append(10)
# print(new_linked_list.length)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

# PRINT LINKED LIST METHOD - to be able to do this first we create a temp node consisting of where the head is pointing (which is the first node) and a results variable where we will append the value of each node to represent the linked list. The temp node will iterate over the linked list appending/concatenating the value of the node to the result and then incrementing the temp node to the next node until the temp node is not None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # PRINT LINKED LIST METHOD
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '-->'
            temp_node = temp_node.next 
        return result

    # APPEND A NEW NODE TO THE LIST
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # PREPEND A NEW NODE TO THE LIST
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # INSERT METHOD IN LINKED LIST
    def insert(self, value, index):
        # MY CODE - CONSIDERING +ve EDGE CASES (Doesn't work for index <= 0)
        # new_node = Node(value)
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     temp_node = self.head
        #     prev_node = temp_node
        #     counter = 0
        #     while counter != index - 1:
        #         prev_node = temp_node
        #         temp_node = temp_node.next
        #         counter += 1
        #     new_node.next = temp_node
        #     prev_node.next = new_node            
        new_node = Node(value)
        if index < 0:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 2):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    # TRAVERSE A LINKED LIST
    def traverse(self):
        counter = 0
        temp_node = self.head
        for _ in range(self.length):
            temp_node = temp_node.next
            counter += 1
        return counter
    
    def search(self, target):
        # MY CODE
        # current = self.head
        # counter = 0
        # for _ in range(self.length):
        #     if current.value != target:
        #         current = current.next
        #         counter += 1
        #     else:
        #         return current.value, counter
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return True
            current = current.next
            index += 1
        return False
    
    # GET METHOD IN LIST
    def get(self, index):
        current = self.head
        counter = 0
        if self.length > index and index >= 0:
            while counter != index:
                current = current.next
                counter += 1
            return current
        elif index < 0 or self.length < index:
            return f"Kindly enter correct value of index within 0 and {self.length}"
    
    def set(self, index, value):
        current = self.head
        counter = 0
        if index >= 0 and index < self.length:
            while counter != index:
                current = current.next
                counter += 1
            current.value = value
        elif index < 0 or index > self.length:
            return f"Kindly enter correct value of index within 0 and {self.length}"
        # temp = self.get(index)
        # if temp:
        #     temp = value
        #     return True
        # return False
        
    def popFirst(self):
        if self.length != 1:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return f"Removed Node: {(popped_node.value, popped_node.next)}"
        else:
            self.head = None
            self.tail = None
        self.length -= 1
    def pop(self):
        if self.length != 1:
            current = self.head
            prev = current
            while current.next is not None:
                prev = current
                current = current.next
            popped_node = (current.value, None)
            prev.next = None
            return f"Removed Node: {popped_node}"
        else:
            self.head = None
            self.tail = None
        self.length -= 1

    def remove(self, index):
        prev_node = self.get(index - 1)
        popped_node = self.get(index)
        prev_node = popped_node.next
        popped_node.next = None

    def deleteAll(self):
        self.head = None
        self.tail = None
        self.length = 0
        # Elements deleted by garbage collector

new_linked_list = LinkedList()
print(new_linked_list)
new_linked_list.prepend(30)
new_linked_list.prepend(20)
new_linked_list.prepend(10)
new_linked_list.insert(40, 4)
print(new_linked_list) 
print(new_linked_list.traverse())
print(new_linked_list.search(90))
print(new_linked_list.get(1))
print(new_linked_list.set(1, 90))
print(new_linked_list.remove())
print(new_linked_list)
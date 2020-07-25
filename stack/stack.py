"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1. Implement Stack class using an array
arr = [1,2,3,4,5]

class Stack:
    def __init__(self):
        self.storage = []  
        #self.storage = arr
    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()

# # Check
# arra = Stack()
# print(arra.storage)
# arra.push(6)
# print(arra.storage)
# arra.pop()
# print(arra.storage)
# arra.push(2)
# arra.push(4)
# print(arra.storage)
# print(arra.__len__())

# 2. Implement a Stack class using Linked List

# import sys
# # ('../singly_linked_list')
# #sys.path.append('C:/Users/Todd/Desktop/data_structures/Data-Structures/singly_linked_list/singly_linked_list.py')            
# sys.path('/singly_linked_list')
# from singly_linked_list import LinkedList 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def __repr__(self):
        return self.value 

    # add get method
    def get_value(self):
        return self.value

    # get next node
    def get_next(self):
        return self.next

    # set next node
    def set_next(self, new_next):
        self.new_next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node 

    def add_to_tail(self, value):
        new_node = Node(value)
        
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
    
        if self.head is None and self.tail is None:
            return 
        
        if not self.head.get_next():
            head = self.head 
            self.head = None
            self.tail = None
            return head.get_value()

        val = self.head.get_value()
        self.head = self.head.get_next()
        return val 

    def llprint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next

    def remove_tail(self):

        if self.head is None and self.tail is None:
            return 
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        val = self.tail.get_value()
        self.tail = current
        return val

# print out a linked list
llist = LinkedList()
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

llist.head = first_node 
first_node.next = second_node
second_node.next = third_node

llist.llprint()

class LLStack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList() 

    def __repr__(self):
        return self.storage  
        
    def __len__(self):
        return self.size 

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        # check to see if empty stack
        if self.size == 0:
            return None
        else:
            self.size -=1
            return self.storage.remove_head()

x = LLStack()
print(x.size)

x.push(6)
print(x.storage)

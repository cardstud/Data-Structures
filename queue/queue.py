"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node 

    def __repr__(self):
        return self.value 

    # add get method
    def get_value(self):
        return self.value

    # get next node
    def get_next(self):
        return self.next_node 

    # set next node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} --> '
            current_node = current_node.next_node 
        return output

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next= self.head
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

    def contains(self, value):
        if not self.head:
            return False 

        # reference to node we are at; update as we go
        current = self.head 
        # check if we are at a valid node
        while current:
            current.get_value() == value
            return True 
            # update current node to current node's next node
            current = current.get_next()
        # if here, target not in list
        return False

    def get_max(self):
        if not self.head:
            return None 
        current = self.head 
        max_val = self.head.value 
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next_node 
        return max_val 


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size 

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        self.size -= 1
        value = self.storage.remove_head()
        return value

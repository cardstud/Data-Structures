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
arr = [1,4,8,16,22]

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.storage = arr 

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop()

# test it

print('------------------------')
arra = Stack()
print(arra.storage)
print(arra.__len__())
arra.push(234)
arra.push(254)
arra.push(1)
arra.push(44)
print(arra.__str__())
print(arra.storage)
arra.pop()
print(arra.storage)

# 2. Implement a Stack class using Linked List
# Using class Node and class LinkedList() here instead of importing

class Node:
    def __init__(self, value, next_node=None):
        # value that the node is holding
        self.value = value

        # ref to the next value
        self.next_node = next_node

    def __str__(self):
        return str(self.value) 

    def get_value(self):
        """
        Method to get a value from the node
        """
        return self.value 

    def get_next(self):
        """
        Method to get a value from the next node
        """
        return self.next_node 

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} -->'
            current_node = current_node.next_node 
        return output

    def add_to_tail(self, value):
        """Add to Tail:
        1. wrap value you are adding in new_node
        2. check if LL empty
            a. if LL empty: (check first)
                    - set self.head to new_node value
                    - set self.tail to new_node value
            b. if at least 1 item already in the LL
                    - update previous last nodes pointer("next_node") to point to the new node (new tail value)
                    - update self.tail value to the new value we added to the tail
        """
        # wrap the value in a new Node
        new_node = Node(value)

        # check if LL is empty
        #   a. if empty, set head and tail to the new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node 

        #   b. else it already has at least 1 item in it
        else:
            # update the last node's "next_node" to the "new_node"
            self.tail.set_next(new_node)  # last node in chain.next_node = new_node 
            # update the self.tail value to point to the new_node value we just added
            self.tail = new_node 

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node 

    def remove_tail(self):
        """
        Remove the last node in the chain and return its value:
        1. Check if LL empty
            a. if LL empty: 
                - set self.head to None
                - set self.tail to None
            
            b. if list has only 1 item:
                - store the value of the node that we are going to remove
                - remove the node
                - set head and tail to None
                - return the store value

            c. if list has more than 1 item:
                - store the value of the node that we are going to remove
                - set the 'self.tail' to the second-to-last node (need to traverse list from start to end)
                    - starting from head
                    - keep iterating until the node after "current_node" is the tail
                    - at end of iteration, set "self.tail" to the "current_node"
                    - set the new tail's "next_node" to None
                - return value
        """
        # check if empty list to start
        if self.head is None and self.tail is None:
            # return None
            return None

        # check if the list only has one item
        if self.head == self.tail:
            # need to store the value of the node we are going to remove
            value = self.tail.get_value()

            # then remove the node by setting head and tail to None
            self.head = None
            self.tail = None 

            # return the stored value
            return value 

        # otherwise
        else:
            # store the value of the node we are going to remove
            value = self.tail.get_value()

        #   We need to set the self.tail to second-to-last-node:
        #   can only do this by traversing the linked list from beginning to end, can only go forward

            # starting from the head
            current_node = self.head 

            # keep iterating until the node after "current_node" is the tail - keep track of it until we get to the node before tail node
            while current_node.get_next() != self.tail:
                # keep looping
                current_node = current_node.get_next()

            # at end of iteration, set "self.tail" to the "current_node" 
            self.tail = current_node

            # set the new tail's "next_node" to None 
            self.tail.set_next(None)

            # return the value 
            return value 

    def remove_head(self):
        """Remove head
        1. check if list is empty
            a. if empty:
                return None

            b. if list has only 1 item:
                - store the value of the node that we are going to remove
                - remove the node
                - set head and tail to None
                - return the store value

            c. if list has more than 1 item
                - store the old head's value
                - set self.head to old head's next node
                - return the value
        """
        # check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None 

        # check if the list only has one item
        if self.head == self.tail:
            # need to store the value of the node we are going to remove
            value = self.head.get_value()

            # then remove the node by setting head and tail to None
            self.head = None
            self.tail = None 

            # return the stored value
            return value 

        else:
            # store the old head's value  (no need to traverse list this time since starting at head)
            value = self.head.get_value()

            # set self.head to old head's next
            self.head = self.head.get_next()

            # return the value
            return value 


# Test it
llist = LinkedList()
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

llist.head = first_node 
first_node.next_node = second_node
second_node.next_node = third_node 

class LLstack:
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
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

    def display(self):
        iternode = self.storage.head 
        while iternode != None:
            print(iternode.value, "->", end="")
            iternode = iternode.next_node  

print('------------------------')   
x = LLstack()
# print(x.size)
# x.push(6)
# x.push(44)
# x.push(45)
# print(x.__str__())
# print(x.storage)

x.push(8)
x.push(22)
x.push("a")
print(x.display())

"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

Their time complexities will be different.

Stack backed by singly-linked list:
    The cost to push or pop into a LL stack is O(1) worst case

Stack backed by a dynamic array:
    The worst case scenario pushing is O(n) and popping is O(1)
    

"""
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """ Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is pointing to """
    def insert_after(self,value):
        current_next = self.next 
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next 
    
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is pointing too."""
    def insert_before(self, value):
        current_prev = self.prev 
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev 

    """ Rearranges this ListNode's previous and next
    pointers accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next:
            self.next.prev = self.prev 
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def display(self):
        # current node will point to head
        current = self.head
        if self.head == None:
            print("List is empty")
            return
        print("-------------")
        print("Nodes of DLL: ")
        print("-------------") 
        while current != None:
            # prints each node by incrementing pointer
            print(current.value,"--> ", end="")
            current = current.next 

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # 1. Remove pointer that old head has to previous (<-- previous arrow)
    # 2. Add new value to point to old head (new_node --> next_node)
    # 3. Have old head point to new head (<-- previous arrow)
    def add_to_head(self, value):
        # our new value we want to add as the new head
        new_node = ListNode(value)

        # increment the length
        self.length += 1

        # check if list is empty
        if self.head is None and self.tail is None:
            # make new value(new_mode) the new head and tail
            self.head = new_node
            self.tail = new_node
           
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node
        

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if not self.head and not self.tail:
        #     return None 
        # else:
        value = self.head.value 
        self.delete(self.head)
        return value 

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value) 
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node 
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
     
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if not self.head and not self.tail:
        #     return None 
        # else:
        value = self.tail.value
        self.delete(self.tail)
        return value    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # def move_to_front(self, node):
    #     if node is self.head:
    #         return None 
    #     value = node.value
    #     if node is self.tail:
    #         self.remove_from_tail()
    #         # self.add_to_head(value) # why not have this line? Gets error.
    #     else:
    #         node.delete()
    #         self.length -= 1
    #     self.add_to_head(value)
        
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value 
        if node is self.tail:
            self.remove_from_tail()
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev 
            
            self.length -= 1
        self.add_to_head(value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    # def move_to_end(self, node):
    #     if node is self.tail:
    #         return 
    #     value = node.value 
    #     if node is self.head:
    #         self.remove_from_head()
    #         self.add_to_tail(value)
    #     else:
    #         node.delete() 
    #         self.length -= 1
    #         self.add_to_tail(value)

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value 
        if node is self.head:
            self.remove_from_head()
        else:
            if node.prev:
                node.prev.next = node.next 
            if node.next:
                node.next.prev = node.prev

            self.length -= 1
        self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    # def delete(self, node):
    #     # check for emtpy
    #     if not self.head and not self.tail:
    #         return
    #     # check if one item in list (head=tail)
    #     if self.head is self.tail:
    #         self.head = None
    #         self.tail = None
    #     elif self.head is node:
    #         self.head = node.next
    #         if node.prev:
    #             node.prev.next = node.next
    #         if node.next:
    #             node.next.prev = node.prev 
    #     elif self.tail is node:
    #         self.tail = node.prev
    #         if node.prev:
    #             node.prev.next = node.next
    #         if node.next:
    #             node.next.prev = node.prev
    #     else:
    #         if node.prev:
    #             node.prev.next = node.next 
    #         if node.next:
    #             node.next.prev = node.prev 
    #     self.length -= 1

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete() 
        elif self.tail == node:
            self.tail = node.prev
            node.delete() 
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value 
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value 
            current = current.next 
        return max_value  

# TEST 
b = DoublyLinkedList()
first_node = ListNode(166)
second_node = ListNode(5)
third_node = ListNode(2)
fourth_node = ListNode(89)

b.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print(b.display())


print('The max of this Doubly list is: ', b.get_max())

a = DoublyLinkedList()
a.display()
class Node:
    def __init__(self, value=None, next_node=None):
        # the value at his linked list node
        self.value = value
        # reference to the next node in the  list
        self.next_node = next_node 

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
        # reference to head of list
        self.head = None
        # reference to tail of list
        self.tail = None

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'{current_node.value} --> '
            current_node = current_node.next_node 
        
        return output

    def add_to_head(self, value):
        # create new node
        new_node = Node(value, None)
        # check if list is empty
        if not self.head:
            self.head = new_node 
            self.tail = new_node 
        else:
            new_node.set_next = self.head 
            self.head = new_node

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value, None)
        # These three steps assume that the tail is already referring to a node (so wont work in all cases if it is not)
        # So what do we do if tail is equal to None?
        # What is rule we want to set to indicate the linked list is empty?
        # Would it be better to check head? well lets just check them both to see if no head or tail
        if not self.head:
            # in a one element linked list, what should head and tail be pointing to?
            # have both head and tail referring to the single node
            self.head = new_node
            # if no tail, set the new node to be the tail
            self.tail = new_node 
        else:
            # 2. set the old tail's 'next' to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node
            self.tail = new_node

    # let's remove from the head
    def remove_head(self):
        # if we have an empty linked list
        if not self.head:
            return None 
        # what if only 1 element in the linked list?
        # so both head and tail are pointing at the same node
        if not self.head.get_next():
            head = self.head 
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list tail reference
            self.tail = None
            return head.get_value()

        value = self.head.get_value()
        # set self.head to the node after the head
        self.head = self.head.get_next()
        return value 

    # lets remove from the tail
    def remove_tail(self):
        # if we have an empty linked list
        if not self.head:
            return None 

        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        # if we have a non-empty linked list(ll) then:
        #    a. set the tail to be None
        #    b. move self.tail to the Node before it
        #          we cant just - 1 since it does not know what points to it
        #          we have to start at the head and move down the linked list
        #             until we get to the node right before the tail
        #           We need to iterate over our linked list
        #           We generally will use a While loop 
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()
        # at this point, current is the node right before the tail
        # so set tail to None
        value = self.tail.get_value()
        # self.tail = None  # technically dont need this step since we are going to make self.tail = current; so can remove
        # move self.tail to the Node right before
        self.tail = current
        return value 

    def contains(self, value):
        if not self.head:
            return False 
        # recursive solution
        # def search(node):
        #     if node.get_value() == value:
        #         return True
            
        #     if not node.get_next():
        #         return False 
        #     return search(node.get_next())
        # return search(self.head)
        # # reference to node we are at; update as we go
        current = self.head 
        # check if we are at a valid node
        while current:
            # return True if current value we are looking for
            if current.get_value() == value:
                return True 
            # update current node to current node's next node
            current = current.get_next()
        # if here, target not in list
        return False

    def get_max(self):
        if not self.head:
            return None 
        # reference to the largest value we've seen so far
        max_value = self.head.value 
        # reference to our current node as we traverse the list 
        current = self.head.get_next()
        # check to see if still at a valid node
        while current:
            # check to see if the current value is > than max
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node
            current = current.get_next()   
        return max_value

    # def get_max(self):
    #     if not self.head:
    #         return None 
    #     current = self.head 
    #     max_val = self.head.value 
    #     while current:
    #         if current.value > max_val:
    #             max_val = current.value
    #         current = current.next_node 
    #     return max_val 


    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.value) 
            temp = temp.next_node

    def llprint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next
    
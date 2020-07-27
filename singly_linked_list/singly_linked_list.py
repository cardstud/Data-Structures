class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

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

    def add_to_tail(self, value):
        # 1. create the Node from the value
        new_node = Node(value)
        # These three steps assume that the tail is already referring to a node (so wont work in all cases if it is not)
        # So what do we do if tail is equal to None?
        # What is rule we want to set to indicate the linked list is empty?
        # Would it be better to check head? well lets just check them both to see if no head or tail
        if self.head is None and self.tail is None:
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
        if self.head is None and self.tail is None:
            return None 
        # what if only 1 element in the linked list?
        # so both head and tail are pointing at the same node
        if not self.head.get_next():
            head = self.head 
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list tail reference
            #self.tail = None
            return head.get_value()

        val = self.head.get_value()
        # set self.head to the node after the head
        self.head = self.head.get_next()
        return val 



    # lets remove from the tail
    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return 
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
        val = self.tail.get_value()
        # self.tail = None  # technically dont need this step since we are going to make self.tail = current; so can remove
        # move self.tail to the Node right before
        self.tail = current
        return val 
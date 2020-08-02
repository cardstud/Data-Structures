"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # instantiate new_node with value
        new_node = BSTNode(value=value)
        # if value is less than root value
        if self.value > value:
            # If self.left doesn't exist, set to new node
            if self.left is None:
                self.left = new_node 
                return
            # Else, use recursion on self.left
            else:
                self.left.insert(value)
        # if value is greater than root value
        else:
            # if self.right doesnt exist, set it to new node  
            if self.right is None:
                self.right = new_node 
                return 
            # else, use recursion on self.right
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value equals target
        if self.value == target:
            return True 
        # Case 2: self.value is greater than target
        if self.value > target:
            if self.left is None:
                return False 
            else:
                return self.left.contains(target)
        # Case 3: self.value is less than target
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # iterative approach
        current = self
        max_val = 0
        if current is None:
            return max_val
        while current is not None:
            max_val = current.value 
            current = current.right
        return max_val 

        # # Recursive approach
        # if self is None:
        #     return None 
        # if self.right is None:
        #     return self.value 
        # return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Solution with for_each method
        arr = []
        fn = lambda x: arr.append(x)
        self.for_ech(fn=fn)
        arr.sort()
        print(*arr, sep='\n')

        # # other solution
        # if self is None:
        #     return
        # # check if we can move left
        # if self.left is not None:
        #     self.left.in_order_print()()
        # # Visit the node by printing its value
        # print(self.value)

        # # Check if we can't move right
        # if self.right is not None:
        #     self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Use a queue to form a line for the nodes to get in
        # Start by placing the root node in the queue
        queue = [self]

        # Need a while loop to iterate (not recursion for BFT)
        while len(queue) > 0:
            # dequeue item from front of queue
            # print its value
            temp = queue.pop(0)
            print(temp.value)

            # place current item's left node in queue if not None
            if temp.left is not None:
                queue.append(temp.left)
            # place current item's right node in the queue if not None
            if temp.right is not None:
                queue.append(temp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # Solution with for_each method (recursive)
        fn = lambda x: print(x)
        self.for_each(fn=fn)

        # iterative approach
        # create a stack to put nodes in, start with root node in it
        stack = [self]

        # While loop to manage iteration
        while len(stack) > 0:
            # Pop item off stack and print its value
            temp = stack.pop(-1)
            print(temp.value)

            # Place current item's left node in stack if not None
            if temp.left:
                stack.append(temp.left)
            # Place current item's right node in stack if not None
            if temp.right:
                stack.append(temp.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BinarySearchTree(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  

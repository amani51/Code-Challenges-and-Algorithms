# #################### Node class #################### #  


class Node:
    '''
    A Class that creates node with pointer refers to None
    '''

    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue


# #################### Stack class #################### #  

class Stack:
    '''
    A class that uses LinkedList to implement stack , and it has methods:
    1 . constructor that has top argument and size
    2. push(): takes value as argument, and create a node and append it into stack, and increase the size by one 
    3. pop(): Removes the element from the back of the stack and returns it, and decrease the size by one 
    4. peek(): Returns the element at the back of the stack.
    5. empty(): returns True if the stack is empty
    6. get_size(): returns the size of the stack
    '''

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This stack is empty")
    
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

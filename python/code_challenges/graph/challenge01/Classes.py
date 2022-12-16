from collections import deque

class Node:
    '''
    A Class that creates a vertex of graph and returns it's value 
    '''
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    '''
    A Class that creates an edge of graph : it takes a vertex and weight as arguments 
    '''
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight


class Queue:
    '''
    A Class that creates Queue data structure by using deque method from collections library 
    it has 4 methods :
    1. constructor method to create a new queue
    2. enqueue method to enqueue elements 
    3. dequeue method to dequeue elements
    4. __len__ method returns the number of elements
    '''
    def __init__(self):
        self.deque1 = deque()

    def enqueue(self,value):
        self.deque1.append(value)

    def dequeue(self):
        return self.deque1.popleft()

    def __len__(self):
        return len(self.deque1)


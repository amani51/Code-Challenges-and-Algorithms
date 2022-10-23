# Write your test here
import pytest
from challenge01 import delete_node
# #################### Node class #################### #  
class Node:
    "A Class that creates node with pointer refers to None"
    def __init__(self,value):
        self.value = value
        self.next = None

# #################### LinkedList class #################### #  

class LinkedList:
    '''
    A Class that creates a linked list and handles its nodes :
    1. append method to append a new node into a linked list  
    2. all_nodes method returns all nodes as a List 
    '''
    def __init__(self):
        self.head = None
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def all_nodes(self):
        list_of_nodes=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                list_of_nodes.append(current.value)
                current = current.next
        return list_of_nodes
        

def test_delete_last_node(linkedlist_test,node_test):
    linkedlist_test.append(node_test[0])
    assert delete_node(node_test[0]) =="Sorry we can not delete the last node!!"
    linkedlist_test.append(node_test[3])
    assert delete_node(node_test[3]) =="Sorry we can not delete the last node!!" 
    linkedlist_test.append(node_test[1])
    linkedlist_test.append(node_test[2])
    delete_node(node_test[3])
    assert delete_node(node_test[3]) =="the node is deleted!!"


def test_all_nodes(linkedlist_test,node_test):
    assert linkedlist_test.all_nodes()==[]
    for i in range(len(node_test)):
        linkedlist_test.append(node_test[i])  
    assert linkedlist_test.all_nodes()==[1,2,3,4]


# #################### Fixtures #################### #  

@pytest.fixture
def linkedlist_test():
    linkedList = LinkedList()
    return linkedList

@pytest.fixture
def node_test():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    return [node1,node2,node3,node4]
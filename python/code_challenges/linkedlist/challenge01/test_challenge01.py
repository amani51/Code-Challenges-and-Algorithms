# Write your test here
import pytest
from challenge01 import LinkedList,Node


def test_length(linkedlist_test):
    assert linkedlist_test.get_length()=='The linked list has a 0 of nodes'


def test_append_node(linkedlist_test,node_test):
    linkedlist_test.append(node_test[0])
    assert linkedlist_test.get_length()=='The linked list has a 1 of nodes'
    linkedlist_test.append(node_test[1])
    assert linkedlist_test.get_length()=='The linked list has a 2 of nodes'
    linkedlist_test.append(node_test[2])
    linkedlist_test.append(node_test[3])
    assert linkedlist_test.get_length()=='The linked list has a 4 of nodes'


def test_delete_node(linkedlist_test,node_test):
    assert linkedlist_test.get_length()=='The linked list has a 0 of nodes'
    linkedlist_test.append(node_test[2])
    linkedlist_test.append(node_test[3])
    assert linkedlist_test.get_length()=='The linked list has a 2 of nodes'



def test_delete_last_node(linkedlist_test,node_test):
    linkedlist_test.append(node_test[0])
    assert linkedlist_test.delete_node(node_test[0]) =="The linked list should have at least 2 nodes to delete"
    linkedlist_test.append(node_test[3])
    assert linkedlist_test.delete_node(node_test[3]) =="Sorry we can not delete the last node!!" 
    assert linkedlist_test.get_length()=='The linked list has a 2 of nodes'
    linkedlist_test.append(node_test[1])
    linkedlist_test.append(node_test[2])
    linkedlist_test.delete_node(node_test[3])
    assert linkedlist_test.get_length()=='The linked list has a 3 of nodes'


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
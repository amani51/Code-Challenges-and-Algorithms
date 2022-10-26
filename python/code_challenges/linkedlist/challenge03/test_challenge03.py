# Write your test here
import pytest
from Classes import LinkedList,Node
from challenge03 import remove_nth_node

# #################### test remove_nth_node function #################### #  

def test_find_middle_node():
    linkedList1 = LinkedList()
    assert remove_nth_node(linkedList1,1)=="The linked list is empty"
    for i in [1,2,3,4,5]:
        node1 = Node(i)
        linkedList1.append(node1)
    assert linkedList1.all_nodes()==[1,2,3,4,5]
    assert remove_nth_node(linkedList1,4).all_nodes()==[1,3,4,5]
    assert remove_nth_node(linkedList1,1).all_nodes()==[1,3,4]
    assert remove_nth_node(linkedList1,3).all_nodes()==[3,4]


    linkedList2 = LinkedList()
    for i in [1,2]:
        node3 = Node(i)
        linkedList2.append(node3)
    assert linkedList2.all_nodes()==[1,2]
    assert remove_nth_node(linkedList2,1).all_nodes()==[1]
    assert remove_nth_node(linkedList2,1).all_nodes()==[]
    assert remove_nth_node(linkedList2,1)=="The linked list is empty"


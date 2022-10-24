# Write your test here
import pytest
from Classes import LinkedList,Node
from challenge02 import find_middle_node

# #################### test find_middle_node function #################### #  

def test_find_middle_node():
    linkedList1 = LinkedList()
    assert find_middle_node(linkedList1)=="The linked list is empty"
    for i in [1,2,3,4,5]:
        node1 = Node(i)
        linkedList1.append(node1)
    assert linkedList1.all_nodes()==[1,2,3,4,5]
    assert find_middle_node(linkedList1).value==3
    assert linkedList1.mid_nodes(find_middle_node(linkedList1).value)==[3,4,5]

    linkedList2 = LinkedList()
    for i in [1,2,5,7,4,9]:
        node2 = Node(i)
        linkedList2.append(node2)
    assert linkedList2.all_nodes()==[1,2,5,7,4,9]
    assert find_middle_node(linkedList2).value==7
    assert linkedList2.mid_nodes(find_middle_node(linkedList2).value)==[7, 4, 9]

    linkedList3 = LinkedList()
    for i in [1]:
        node3 = Node(i)
        linkedList3.append(node3)
    assert linkedList3.all_nodes()==[1]
    assert find_middle_node(linkedList3).value==1
    assert linkedList3.mid_nodes(find_middle_node(linkedList3).value)==[1]



# Write here the code challenge solution
from Classes import Node, LinkedList

# #################### find_middle_node function #################### #  

def find_middle_node(head_linkedList):
    '''
    A function that takes a linkedList as argument and return the middle node 
    '''
    if head_linkedList.head is None:
        return "The linked list is empty"
    else: 
        mid = head_linkedList.head
        mid_next = head_linkedList.head
        while mid_next is not None and mid_next.next is not None:
            mid = mid.next
            mid_next = mid_next.next.next
        return mid 

# #################### __name__ #################### #  


if __name__=="__main__":
    

    linkedList1 = LinkedList()
    for i in [1,2,5,4,9]:
        node1 = Node(i)
        linkedList1.append(node1)
    linkedList2 = LinkedList()
    for i in [1,2,5,7,4,9]:
        node2 = Node(i)
        linkedList2.append(node2)
    linkedList3 = LinkedList()
    for i in [1,2,5,7,4,9,3,8]:
        node3 = Node(i)
        linkedList3.append(node3)
    

    print("\n***************************************************\n")
    print("We have a likedList with nodes => ",linkedList1.all_nodes()) 
    print("The middle node is => ",find_middle_node(linkedList1).value)
    print("Now a likedList with middle nodes => ",linkedList1.mid_nodes(find_middle_node(linkedList1).value)) 

    print("\n***************************************************\n")
    print("We have a likedList with nodes => ",linkedList2.all_nodes()) 
    print("The middle node is => ",find_middle_node(linkedList2).value)
    print("Now a likedList with middle nodes => ",linkedList2.mid_nodes(find_middle_node(linkedList2).value)) 
    
    print("\n***************************************************\n")
    print("We have a likedList with nodes => ",linkedList3.all_nodes()) 
    print("The middle node is => ",find_middle_node(linkedList3).value)
    print("Now a likedList with middle nodes => ",linkedList3.mid_nodes(find_middle_node(linkedList3).value)) 
    print("\n***************************************************\n")
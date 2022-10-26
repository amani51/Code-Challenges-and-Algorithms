# Write here the code challenge solution
from Classes import Node, LinkedList

# #################### remove_nth_node function #################### #  

def remove_nth_node(ll,n):
    '''
    A function that takes a head of a linked list and the nth node , remove the nth node from the end of the list.
    '''
    if ll.head is None:
            return "The linked list is empty"
    else: 
        slow = ll.head
        fast = ll.head
        for i in range(n):
            if fast.next is None:
                if i==(n-1):
                    ll.head = ll.head.next
                return ll
            fast = fast.next   
        while fast.next is not None:
            fast = fast.next
            slow = slow.next  
        slow.next = slow.next.next

    return ll




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
    print("Delete the last Node from the end ")
    print("Now a likedList has  => ",remove_nth_node(linkedList1,5).all_nodes()) 

    print("\n***************************************************\n")
    print("We have a likedList with nodes => ",linkedList2.all_nodes()) 
    print("Delete the first Node from the end")
    print("Now a likedList has => ",remove_nth_node(linkedList2,1).all_nodes())
    
    print("\n***************************************************\n")
    print("We have a likedList with nodes => ",linkedList3.all_nodes()) 
    print("Delete the 3th Node from the end ")
    print("Now a likedList has => ",remove_nth_node(linkedList3,3).all_nodes()) 
    print("\n***************************************************\n")
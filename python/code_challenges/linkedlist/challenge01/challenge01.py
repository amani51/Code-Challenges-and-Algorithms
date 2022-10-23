
def delete_node( node):
    '''
    A function that takes a node as argument and delete it from a linked list 
    '''
    if node.next is not None:
        node.value = node.next.value
        node.next = node.next.next
        return "the node is deleted!!"
    else:
        return "Sorry we can not delete the last node!!" 

if __name__=="__main__":
    from test_challenge01 import Node,LinkedList
    # create linkedList object and 6 nodes objects ,and append all nodes into linkedList 
    linkedList1 = LinkedList()
    node1 = Node(1)
    linkedList1.append(node1)
    node2 = Node(2)
    linkedList1.append(node2)
    node3 = Node(-3)
    linkedList1.append(node3)
    node4 = Node(50)
    linkedList1.append(node4)
    node5 = Node(-54)
    linkedList1.append(node5)
    node6 = Node(0)
    linkedList1.append(node6)
    # output terminal 
    print("\n***************************************************\n")
    print("we have a likedList with nodes => ",linkedList1.all_nodes()) # print the linkedList as list 
    print("\n**************************************************\n")
    print('Delete node 2')
    print(delete_node(node2))
    print("A likedList after delete node 2 => ",linkedList1.all_nodes()) 
    print("\n***************************************************\n")
    print('Delete node 4')
    print(delete_node(node5))
    print("A likedList after delete node 4 => ",linkedList1.all_nodes()) 
    print("\n***************************************************\n")
    print('Delete the last node')
    print(delete_node(node5))
    print("A likedList after trying to delete last node => ",linkedList1.all_nodes()) 
    print("\n***************************************************\n")

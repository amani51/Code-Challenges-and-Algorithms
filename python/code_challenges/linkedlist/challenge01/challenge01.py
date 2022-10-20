# #################### Node class #################### #  
class Node:
    "A Class that creates node with pointer refers to None"
    def __init__(self,value):
        self.value = value
        self.next = None

# #################### LinkedList class #################### #  
from locale import currency


class LinkedList:
    '''
    A Class that creates a linked list and handles its nodes :
    1. append method to append a new node into a linked list  
    2. delete_node method to delete a specific node from the linked 
    3. all_nodes method returns all nodes as a List
    4. get_length method returns the number of nodes inside the linked list  
    '''
    def __init__(self):
        self.head = None
        self.length=0
    def append(self, node):
        if self.head is None:
            self.head = node
            self.length+=1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            self.length+=1

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


    def delete_node(self, node):
        if self.length<2:
            return "The linked list should have at least 2 nodes to delete"
        elif node.next is not None:
            self.length-=1
            node.value = node.next.value
            node.next = node.next.next
            return "the node is deleted!!"
        else:
           return "Sorry we can not delete the last node!!"       

    
    def get_length(self):
        return  f'The linked list has a {self.length} of nodes'


if __name__=="__main__":
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
    print(linkedList1.get_length()) # print the number of nodes 
    print("\n**************************************************\n")
    print('Delete node 2')
    print(linkedList1.delete_node(node2))
    print("A likedList after delete node 2 => ",linkedList1.all_nodes()) 
    print(linkedList1.get_length()) # print the number of nodes 
    print("\n***************************************************\n")
    print('Delete node 4')
    print(linkedList1.delete_node(node5))
    print("A likedList after delete node 4 => ",linkedList1.all_nodes()) 
    print(linkedList1.get_length()) # print the number of nodes 
    print("\n***************************************************\n")
    print('Delete the last node')
    print(linkedList1.delete_node(node5))
    print("A likedList after trying to delete last node => ",linkedList1.all_nodes()) 
    print(linkedList1.get_length()) # print the number of nodes 
    print("\n***************************************************\n")

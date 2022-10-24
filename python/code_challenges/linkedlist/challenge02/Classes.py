
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
    2. delete_node method to delete a specific node from the linked 
    3. all_nodes method returns all nodes as a List  
    4. mid_nodes method returns middle nodes of linkedList 
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


    def mid_nodes(self,x):
        list_of_nodes=[]
        if self.head is None:
            return "The linked list is empty"
        else:
            current = self.head
            while current is not None:
                list_of_nodes.append(current.value)
                current = current.next
        i=list_of_nodes.index(x)
        return list_of_nodes[i:]
    
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


    def delete_node(self,node):
        if node.next is not None:
            node.value = node.next.value
            node.next = node.next.next
            return "the node is deleted!!"
        else:
            return "Sorry we can not delete the last node!!" 
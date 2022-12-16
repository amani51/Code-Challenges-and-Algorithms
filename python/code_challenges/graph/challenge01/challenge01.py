# Write here the code challenge solution
from Classes import  Node,Edge,Queue
class Graph:
    '''
    A Class that creates a graph of vertices and edges 
    '''
    def __init__(self):
        '''
        A constructor to create an empty directory 
        '''
        self.adj_list = {}

    def add_node(self,value):
        '''
        A method to create a key (vertex as argument) in the adj_list with empty list as value 
        '''
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        '''
        A method to create a connection between two vertices..
        it takes 3 arguments vertices and weight of the connection
        '''
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        '''
        A str method to print a adj_list 
        '''
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output

    def breadth_first(self, root):
        '''
        A method that take a value as argument, then traverse through the graph using Breadth First way starting from the inputted value, 
        and appending all the visited nodes values in a returned array
        '''
        nodes = []
        breadth = Queue()
        visted = set()

        breadth.enqueue(root)
        visted.add(root)

        while len(breadth):
            front = breadth.dequeue()
            nodes.append(front.value)

            for edge in self.adj_list[front]:
                if edge.vertex not in visted:
                    breadth.enqueue(edge.vertex)
                    visted.add(edge.vertex)

        return nodes

if __name__ == "__main__":
    
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    d = graph.add_node('D')
    e = graph.add_node('E')
    f = graph.add_node('F')
    g = graph.add_node('G')
    h= graph.add_node('H')
    i= graph.add_node('I')
    k= graph.add_node('K')

    graph.add_edge(a,c)
    graph.add_edge(a,e)
    graph.add_edge(a,b)

    graph.add_edge(c,f)
    graph.add_edge(b,d)
    graph.add_edge(e,g)
    graph.add_edge(e,d)
    graph.add_edge(e,f)

    graph.add_edge(f,i)
    graph.add_edge(g,h)
    graph.add_edge(f,h)

    graph.add_edge(i,k)
    graph.add_edge(h,k)

    print('\n# #################### breadth_first method #################### #\n')
    print('We have a Graph\n')
    print(graph)
    print('> root = A')
    print('\nBreadth First => ',graph.breadth_first(a))
    print('\n***********************************************************')


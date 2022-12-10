# Write here the code challenge solution
from Classes import * 

def two_sum_bst(root, k):
    '''
    A function that takes a Binary Search tree and an integer as a parameter. 
    Return True if Binary search tree has two elements that their summation is the given integer
    '''    
    def inner(root):
        if not root:
            return False
        if k - root.value in nodes:
            return True
        nodes.add(root.value)
        return inner(root.left) or inner(root.right)
    nodes = set()
    return inner(root)

if __name__ =='__main__':
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2) 
    x=bfs([],tree.root)
    print('\n# #################### two_sum_bst function #################### #\n')
    print('> root =',x)
    print('\n\tk=4 => ',two_sum_bst(tree.root, 4))
    print('\n\tk=9 => ',two_sum_bst(tree.root, 9))
    print('\n\tk=5 => ',two_sum_bst(tree.root, 5))
    print('\n***********************************************************')
    tree2=Tree()
    tree2.root = Node(7)
    tree2.root.left = Node(2)
    tree2.root.right = Node(9)
    tree2.root.right.right = Node(14)
    tree2.root.left.right = Node(5)
    tree2.root.left.left = Node(1) 
    y=bfs([],tree2.root)
    print('> root =',y)
    print('\n\tk=3 => ',two_sum_bst(tree2.root, 3))
    print('\n\tk=4 => ',two_sum_bst(tree2.root, 4))
    print('\n\tk=9 => ',two_sum_bst(tree2.root, 9))
    print('\n***********************************************************')
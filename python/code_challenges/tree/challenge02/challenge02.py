# Write here the code challenge solution
from Classes import Node , Tree ,pre_order

def bft(p,q):
    if not p and not q:
            return True
    if not p or not q:
        return False
    return p.value==q.value and  bft(p.left,q.left) and bft(p.right,q.right)

if __name__ == "__main__":
    tree=Tree()
    tree.root = Node(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    # tree.root.right.left = Node(15)
    # tree.root.right.right = Node(7)
    tree1=Tree()
    tree1.root = Node(3)
    tree1.root.left = Node(9)
    tree1.root.right = Node(20)
    # tree1.root.left.right = Node(8)
    # tree1.root.left.left = Node(10)
    print('\n# #################### btf function #################### #\n')
    print('We have a first tree with => ',pre_order([],tree.root),'\n')
    print('We have a second tree with => ',pre_order([],tree1.root),'\n')
    print('Are they the same tree: ',bft(tree.root,tree1.root))
    print('\n***********************************************************')
    print('\nsecond example:\n')
    print('***********************************************************\n')
    tree1.root.left.right = Node(8)
    tree.root.left.left = Node(10)
    print('We have a first tree with => ',pre_order([],tree.root),'\n')
    print('We have a second tree with => ',pre_order([],tree1.root),'\n')
    print('Are they the same tree: ',bft(tree.root,tree1.root))
    print('\n***********************************************************\n')

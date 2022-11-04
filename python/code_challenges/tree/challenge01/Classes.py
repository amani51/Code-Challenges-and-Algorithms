# #################### Node Class #################### #

class Node():
    '''
    A class that represents a node in the tree structure and it takes value ,left ,right as arguments 
    '''
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

# #################### Tree Class #################### #

class Tree():
    '''
    A class that represents a binary tree 
    '''
    def __init__(self):
        self.root = None

# #################### Depth First ways #################### #

def pre_order(p,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows Pre-order algorithm    
    '''
    if root:
        p.append(root.value)
    if root.left:
        pre_order(p,root.left)
    if root.right:
        pre_order(p,root.right)
    return p

def in_order(i,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows in-order algorithm
    '''
    if root.left:
        in_order(i,root.left) 
    if root:
        i.append(root.value)
    if root.right:
        in_order(i,root.right)
    return i

def post_order(po,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows post-order algorithm    
    '''
    if root.left:
        post_order(po,root.left) 
    if root:
        po.append(root.value)
    if root.right:
        post_order(po,root.right)
    return po

# #################### Breadth First way #################### #

def bfs(bf,root):
    '''
    A function that takes a root node of tree and and list as arguments 
    and returns a list of the value of the nodes by follows Breadth first algorithm    
    '''
    if not root:
        bf.append(None)
        return
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.left :
            queue.append(current.left)
        if current.right :
            queue.append(current.right)
        bf.append(current.value)
    return bf
    
# #################### __name__ side #################### #

if __name__ == '__main__':
    tree=Tree()
    tree.root = Node(3)
    tree.root.left = Node(9)
    tree.root.right = Node(20)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(8)
    tree.root.left.left = Node(10)
    print('pre_order =>',pre_order([],tree.root))
    print('in_order => ',in_order([],tree.root))
    print('post_order => ',post_order([],tree.root))
    print('bfs => ',bfs([],tree.root))
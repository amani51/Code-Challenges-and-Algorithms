# Write here the code challenge solution

from Classes import Node,Tree,pre_order,in_order,bfs 

# #################### pre_in_order function #################### #

def pre_in_order(pre,in_o):
    '''
    A function that takes two lists [pre-order] and [in-order] as arguments 
    and return a root of the tree
    '''
    if len(pre) == 0  or len(in_o) == 0:
            return None
    else:
        root=pre[0]
        index=in_o.index(root)
        in_left=in_o[0:index]
        in_right=in_o[index+1:]
        pre_left=pre[1:len(in_left) + 1]
        pre_right=pre[1 + len(in_left):]
        tree=Tree() 
        tree.root=Node(root,pre_in_order(pre_left, in_left),pre_in_order(pre_right,in_right))
        return tree.root

# #################### __name__ side #################### #

if __name__ == '__main__':
    x=pre_in_order([3, 9, 20, 15, 7],[9, 3, 15, 20, 7])
    print(pre_order([],x))
    print(in_order([],x))
    print(bfs([],x))
    print(bfs([],pre_in_order([-1], [-1])))
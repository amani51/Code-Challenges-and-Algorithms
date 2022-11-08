# Write here the code challenge solution

from Classes import Node,Tree,pre_order,in_order,bfs 

# #################### tree_convert_to_BST Function #################### #

def tree_convert_to_BST(list1):
    '''
    A function that takes an integer list nums, and convert it to a height-balanced binary search tree
    and return the root of the tree 
    '''
    list1.sort()
    def tree_bst(sorted_list):
        tree=Tree()
        if len(sorted_list)==0:
            return 
        elif len(sorted_list)==1:
            mid=sorted_list[0]    
        else:
            mid=sorted_list[len(sorted_list)//2]
        index=sorted_list.index(mid)
        left=sorted_list[:sorted_list.index(mid)]
        right=sorted_list[sorted_list.index(mid)+1:]
        tree.root=Node(mid)
        tree.root.left=tree_bst(left)
        tree.root.right=tree_bst(right)
        return tree.root
    return tree_bst(list1)


# #################### __name__ side  #################### #

if __name__ == '__main__':
    print('\n# #################### tree_convert_to_BST function #################### #\n')
    nums = [7,-5,4,-8,6-4,1,0]
    print('We have a integer list => ',nums,'\n')
    print('The BST will be by using Breadth first => ',bfs([],tree_convert_to_BST(nums)),'\n')
    print('The BST will be by using inorder way => ',in_order([],tree_convert_to_BST(nums)))
    print('\n***********************************************************')
    nums= [0,-1]
    print('\nsecond example:\n')
    print('***********************************************************\n')
    print('We have a integer list => ',nums,'\n')
    print('The BST will be using Breadth first => ',bfs([],tree_convert_to_BST(nums)),'\n')
    print('The BST will be by using inorder way => ',in_order([],tree_convert_to_BST(nums)))
    print('\n***********************************************************\n')


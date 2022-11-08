# Write your test here

from challenge03 import tree_convert_to_BST
from Classes import Node , Tree ,bfs

# #################### test tree_convert_to_BST Function #################### #

def test_tree_convert_to_BST():
    nums1 = [0, -3, -10, 5, 9]
    assert bfs([],tree_convert_to_BST(nums1))==[0, -3, 9, -10, 5]
    nums2= [3, 1]
    assert bfs([],tree_convert_to_BST(nums2))==[3,1]   
    nums3=[1] 
    assert bfs([],tree_convert_to_BST(nums3))==[1]  
    nums4=[] 
    assert bfs([],tree_convert_to_BST(nums4))==None 

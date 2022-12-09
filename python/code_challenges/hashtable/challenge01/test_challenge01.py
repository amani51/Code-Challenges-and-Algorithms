# Write your test here
import pytest
from challenge01 import two_sum_bst
from Classes import *

# #################### test two_sum_bst Function #################### #

def test_two_sum_bst1(tree1):
    assert two_sum_bst(tree1,4)==False
    assert two_sum_bst(tree1,9)==True
    assert two_sum_bst(tree1,5)==True

def test_two_sum_bst2(tree2):
    assert two_sum_bst(tree2,3)==True
    assert two_sum_bst(tree2,4)==False
    assert two_sum_bst(tree2,9)==True



# #################### Fixtures #################### #  

@pytest.fixture
def tree1():
    tree=Tree()
    tree.root = Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right = Node(4)
    tree.root.left.left = Node(2) 
    return tree.root

@pytest.fixture
def tree2():
    tree2=Tree()
    tree2.root = Node(7)
    tree2.root.left = Node(2)
    tree2.root.right = Node(9)
    tree2.root.right.right = Node(14)
    tree2.root.left.right = Node(5)
    tree2.root.left.left = Node(1) 
    return tree2.root
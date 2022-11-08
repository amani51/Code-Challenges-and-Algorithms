# Write your test here
from challenge02 import bft
from Classes import Node , Tree 

def test_bft():
    tree1=Tree()
    tree1.root = Node(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree2=Tree()
    tree2.root = Node(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    assert bft(tree2.root,tree1.root)==True
    tree2.root.right = Node(2)
    assert bft(tree2.root,tree1.root)==False
    tree2.root.right = Node(3)
    tree2.root.left.right = Node(4)
    assert bft(tree2.root,tree1.root)==False


    
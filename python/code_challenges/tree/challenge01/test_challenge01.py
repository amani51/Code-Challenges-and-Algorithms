# Write your test here
from Classes import Node,Tree,pre_order,in_order,bfs
from challenge01 import pre_in_order

def test_pre_in_order():
    x= pre_in_order([3, 9, 20, 15, 7],[9, 3, 15, 20, 7])
    assert pre_order([],x)==[3, 9, 20, 15, 7]
    assert in_order([],x)==[9, 3, 15, 20, 7]
    assert bfs([],x)==[3, 9, 20, 15, 7]
    assert bfs([],pre_in_order([-1], [-1]))==[-1]
    assert bfs([],pre_in_order([], []))==None
    assert bfs([],pre_in_order([1,2,3], [2,1,3]))==[1,2,3]


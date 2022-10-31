# Write your test here
import pytest
from challenge01 import MyQueue

# #################### test remove_nth_node function #################### #  

def test_queue_push(queue1):
    queue1.push(1)
    queue1.push(2)
    queue1.push(3)
    assert queue1.get_queue()==[1,2,3]
    queue1.push(4)
    queue1.push(5)
    queue1.push(6)
    assert queue1.get_queue()==[1,2,3,4,5,6]

def test_queue_pop(queue1):
    queue1.push(0)
    queue1.push(1)
    queue1.push(2)
    assert queue1.pop()==0
    assert queue1.get_queue()==[1,2]
    queue1.push(3)
    queue1.push(4)
    queue1.push(5)
    assert queue1.pop()==1
    assert queue1.pop()==2
    assert queue1.get_queue()==[3, 4, 5]

def test_queue_peek(queue1):
    queue1.push(0)
    queue1.push(1)
    assert queue1.peek()==0
    assert queue1.get_queue()==[0,1]

def test_queue_empty(queue1):
    assert queue1.empty()==True
    queue1.push(1)
    assert queue1.empty()==False

# #################### Fixture #################### #  

@pytest.fixture
def queue1():
    return MyQueue()
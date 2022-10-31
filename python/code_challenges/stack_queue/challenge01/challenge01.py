# Write here the code challenge solution
from Classes import Stack

# #################### MyQueue class #################### #  

class MyQueue:
    '''
    A class that has two stacks (front stack,rear stack) and it contains methods:
        1. push() : Pushes element x to the back of the queue
        2. pop() Removes the element from the front of the queue and returns it.
        3. peek() Returns the element at the front of the queue.
        4. empty() Returns true if the queue is empty, false otherwise
        5. get_queue() Returns the list of elements of the queue
    '''
    def __init__(self):

        self.front = Stack() # first stack
        self.rear = Stack()  # second stack 
        self.queue=[]
    
    def push(self, value):
        if self.rear.get_size() != 0:
            for item in range(self.rear.get_size()):
                self.front.push(self.rear.pop())
        self.queue.append(value)
        self.front.push(value)
        for item in range(self.front.get_size()):
            self.rear.push(self.front.pop())
   
    def pop(self):
        if not self.rear:
            return self.rear 
        self.queue.pop(0)
        return self.rear.pop()

    def peek(self):
        return self.rear.peek()

    def empty(self):
        return self.rear.empty()

    def get_queue(self):
        return self.queue

if __name__=="__main__":

    print('\n************************************** \n\tQueue Class\n**************************************\n')
    myQueue = MyQueue()
    myQueue.push(1)
    print("We have a Queue with first push item =>" ,myQueue.get_queue(),'\n')
    myQueue.push(2)
    print("We have a Queue with second push item =>" ,myQueue.get_queue(),'\n')
    myQueue.push(3)
    myQueue.push(4)
    print("Now push 3 and 4 \n")
    print('The queue will be => ',myQueue.get_queue(),'\n')
    print('**************************************\n')
    print('pop the Queue with "FIFO"=>',myQueue.pop(),'\n')
    print('peek the Queue item with "FIFO"=>',myQueue.peek(),'\n')
    print('pop the Queue again =>',myQueue.pop(),'\n')
    print('**************************************\n')
    print('peek the Queue item with "FIFO"=>',myQueue.peek(),'\n')
    print('The queue will be => ',myQueue.get_queue(),'\n')
    print('Is the queue empty',myQueue.empty())
    print('\n*****************************************************************\n')
    
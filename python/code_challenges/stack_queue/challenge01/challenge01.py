# Write here the code challenge solution


# #################### MyQueue class #################### #  

class MyQueue:
    '''
    A class that has two stacks (front stack,rear stack) and it contains methods:
        1. push() : Pushes element x to the back of the queue
        2. pop() Removes the element from the front of the queue and returns it.
        3. peek() Returns the element at the front of the queue.
        4. empty() Returns true if the queue is empty, false otherwise
        5. get_front() Returns the list of elements of the first stack
        6. get_rear() Returns the list of elements of the second stack
    '''
    def __init__(self):

        self.front = [] # first stack
        self.rear = []  # second stack 
    
    def push(self, value):
        if len(self.rear) != 0:
            for item in range(len(self.rear)):
                self.front.append(self.rear.pop())
        self.front.append(value)

        for item in range(len(self.front)):
            self.rear.append(self.front.pop())
   
    def pop(self):
        if not self.rear:
            return self.rear 
        return self.rear.pop()

    def peek(self):
        if not self.rear:
            return self.rear
        return self.rear[-1]

    def empty(self):
        return len(self.front)== 0 and len(self.rear)== 0
    
    def get_front(self):
        if len(self.rear) != 0:
            for item in range(len(self.rear)):
                self.front.append(self.rear.pop())
        return self.front

    def get_rear(self):
        if len(self.front) != 0:
            for item in range(len(self.front)):
                self.rear.append(self.front.pop())
        return self.rear

if __name__=="__main__":

    print('\n************************************** \n\tQueue Class\n**************************************\n')
    myQueue = MyQueue()
    myQueue.push(1)
    print("We have a Queue with first push item =>" ,myQueue.get_front(),'\n')
    myQueue.push(2)
    print("We have a Queue with second push item =>" ,myQueue.get_front(),'\n')
    myQueue.push(3)
    myQueue.push(4)
    print("Now push 3 and 4 \n")
    print('The first Stack will be => ',myQueue.get_front(),'\n')
    print('The second Stack will be => ',myQueue.get_rear(),'\n')
    print('**************************************\n')
    print('pop the Queue with "FIFO"=>',myQueue.pop(),'\n')
    print('peek the Queue item with "FIFO"=>',myQueue.peek(),'\n')
    print('pop the Queue again =>',myQueue.pop(),'\n')
    print('**************************************\n')
    print('peek the Queue item with "FIFO"=>',myQueue.peek(),'\n')
    print('The first Stack will be => ',myQueue.get_front(),'\n')
    print('The second Stack will be => ',myQueue.get_rear(),'\n')
    print('*****************************************************************\n')
    
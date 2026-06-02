
from linkedList import *

# References - algorithms.py submitted for prac 3- Stacks and Queues
class DSAQueue(DSALinkedList):  # using inheritance becuase the queue is inheriting all functions from DSALinkedList
    def __init__(self): 
        super().__init__()  # calls parentClass DSALinkedLIst and initializes head  None

    def enqueue(self, value):
        self.insertLast(value)

    def dequeue(self):
        if self.peekFirst() is None:  # only calls removeFirst if queue is not empty
            raise Exception("Queue is empty")
        else:
            return self.removeFirst()

    def peek(self):
        return self.peekFirst()

    def printQueue(self):
        self.printLinkedListQueue()


# References - algorithms.py submitted for prac 3- Stacks and Queues
class DSAStack(DSALinkedList):  # using inheritance becuase the stack is inheriting all functions from DSALinkedList
    def __init__(self): 
        super().__init__()  # calls parentClass DSALinkedList and initializes head  to None
        
    def push(self, value):
        self.insertFirst(value)

    def pop(self):
        if self.peekFirst() is None:  # only calls removeFirst if stack is not empty
            raise Exception("Stack is empty")
        else:
            return self.removeFirst()
        

    def top(self): 
        return self.peekFirst()

    def printStack(self):
        self.printLinkedListStack()


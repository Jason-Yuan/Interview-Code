# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from Stack import *

##############################################################################################################################
# Ideas: for dequeue(FIFO), we pop the element for stack 1 and push to stack 2, then pop from stack 2
# Time Complexity: O(1) for enquene / O(n) for dequeue 
# Space Complexity: O(n)
##############################################################################################################################

class MyQueue(object):
    def __init__(self):
        self.firstStack = Stack()
        self.secondStack = Stack()
        
    def enqueue(self, item):
        self.firstStack.push(item)
        
    def dequeue(self):
        if self.secondStack.size() == 0:
            while self.firstStack.size() > 0:
                self.secondStack.push(self.firstStack.pop())
        return self.secondStack.pop()

    def peek(self):
        if self.secondStack.size() == 0:
            while self.firstStack.size() > 0:
                self.secondStack.push(self.firstStack.pop())
        return self.secondStack.peek()

    def isEmpty(self):
        return self.firstStack.size() == 0 and self.secondStack.size() == 0

##############################################################################################################################

def main():
    # initialize a MyQueue
    queue = MyQueue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print "Is my queue empty? ", queue.isEmpty()
    print "The peek of my current queue is: ", queue.peek()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print "The peek of my current queue is: ", queue.peek()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print "The peek of my current queue is: ", queue.peek()

if __name__ == '__main__':
    main()
##############################################################################################################################
#      Project:                  Queue base on python list
##############################################################################################################################

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

##############################################################################################################################

def main():
    # initialize a queue
    myqueue = Queue()

    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    print "Check if the queue is empty? ", myqueue.isEmpty()
    print "Size of my queue: ", myqueue.size()
    print "Pop out an item from the queue: ", myqueue.dequeue()

if __name__ == '__main__':
    main()
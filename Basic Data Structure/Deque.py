##############################################################################################################################
#      Project:                  Queue base on python list
###############################################################################################################################

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

##############################################################################################################################

def main():
    # initialize a deque
    mydeque = Deque()

    mydeque.addFront(1)
    mydeque.addRear(2)
    mydeque.addFront(3)
    mydeque.addRear(4)

    print "Items in mydeque: "
    while not mydeque.isEmpty():
        print mydeque.removeFront()

if __name__ == '__main__':
    main()
##############################################################################################################################
#      Project:                  Stack base on python list
##############################################################################################################################

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

##############################################################################################################################

def main():
    # initialize a stack
    mystack = Stack()

    # push something into the stack
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)

    print "Size of my stack: ", mystack.size()
    print "Top of the stack is: ", mystack.peek()
    print "Pop out an item from stack: ", mystack.pop()
    print "Size of my stack: ", mystack.size()

if __name__ == '__main__':
    main()
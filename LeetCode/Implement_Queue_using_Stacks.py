class Stack(object):
    def __init__(self):
        self.items = []
    
    def empty(self):
        return self.items == []
    
    def push(self, x):
        self.items.append(x)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.InStack = Stack()
        self.OutStack = Stack()
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.InStack.push(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.OutStack.empty():
            return self.OutStack.pop()
        else:
            while not self.InStack.empty():
                self.OutStack.push(self.InStack.pop())
            return self.OutStack.pop()
            
    def peek(self):
        """
        :rtype: int
        """
        if not self.OutStack.empty():
            return self.OutStack.peek()
        else:
            while not self.InStack.empty():
                self.OutStack.push(self.InStack.pop())
            return self.OutStack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        if self.InStack.empty() and self.OutStack.empty():
            return True
        else:
            return False
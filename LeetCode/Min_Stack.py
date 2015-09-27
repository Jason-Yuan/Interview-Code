class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.minstack) == 0 or self.minstack[-1] > x:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self):
        """
        :rtype: nothing
        """
        self.minstack.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
import Queue

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.put(x)
        while self.q2.qsize() != 0:
            self.q1.put(self.q2.get())
        while self.q1.qsize() != 0:
            self.q2.put(self.q1.get())
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.q2.get()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q2.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.q2.qsize() == 0
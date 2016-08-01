import Queue
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.median = None
        self.MaxHeap, self.MinHeap = Queue.PriorityQueue(), Queue.PriorityQueue()
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.median:
            self.median = num
        else:
            if num > self.median:
                self.MinHeap.put(num)
            else:
                self.MaxHeap.put(-num)
                
            if self.MaxHeap.qsize() > self.MinHeap.qsize():
                self.MinHeap.put(self.median)
                self.median = -self.MaxHeap.get()
            if self.MaxHeap.qsize() + 1 < self.MinHeap.qsize():
                self.MaxHeap.put(-self.median)
                self.median = self.MinHeap.get()

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.median:
            return float(0)
        else:
            if self.MaxHeap.qsize() == self.MinHeap.qsize():
                return self.median
            else:
                return (self.median + self.MinHeap.queue[0]) / float(2)
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
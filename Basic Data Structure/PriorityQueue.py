##############################################################################################################################
#      Project:                  Priority Queue
#      Info:                     1. Priority Queue is implemented based on heap data structure
#                                2. A heap data structure is a array which visualized as NEARLY completed binary tree
#                                3. NEARLY - because the outer(last) layer may not be completed
#                                4. Two types of heap: MinHeap and MaxHeap
##############################################################################################################################

class PriorityQueue:
	def __init__(self):
		self.maxheap = [0]
		self.currentSize = 0

	def put(self, data):
		"""add a new item to the maxheap"""
		self.maxheap.append(data)
		self.currentSize += 1
		self.siftUp(self.currentSize)

	def peek(self):
		"""returns the item with the maxmum key value"""
		return self.maxheap[1]

	def get(self):
		"""returns the item with the maxmum key value, removing the item from the heap"""
		res = self.maxheap[1]
		self.maxheap[1] = self.maxheap[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.maxheap.pop()
		self.siftDown(1)
		return res

	def siftUp(self, index):
        # // means devide by 2 and return int
        while index // 2 > 0:
            if self.maxheap[index] < self.maxheap[index // 2]:
                break
            else:
                self.maxheap[index], self.maxheap[index // 2] = self.maxheap[index // 2], self.maxheap[index] 
            index = index // 2

	def siftDown(self, index):
		"""correct single violation in a sub-tree"""
		if index > self.currentSize // 2:
			return
		# find the max child of current index
		if index*2+1 > self.currentSize or self.maxheap[index*2] > self.maxheap[index*2+1]:
			maxChild = index*2
		else:
			maxChild = index*2+1
		if self.maxheap[index] > self.maxheap[maxChild]:
			return
		else:
			self.maxheap[index], self.maxheap[maxChild] = self.maxheap[maxChild], self.maxheap[index]
		self.siftDown(index*2)
		self.siftDown(index*2+1)

	def maxHeapify(self, L):
		"""build a new maxheap from an unordered array"""
		self.currentSize = len(L)
		self.maxheap = [0] + L
		for i in range(len(L)//2, 0, -1):
			self.siftDown(i)

	def size(self):
		return self.currentSize

	def isEmpty(self):
		return self.currentSize == 0

##############################################################################################################################

def main():
    MyPQ = PriorityQueue()
    L = [6, 5, 7, 2, 1, 3, 8]

    MyPQ.maxHeapify(L)
    print "Build a priority queue from a list L: ", L
    print "Size: ", MyPQ.size()

    MyPQ.put(15)
    MyPQ.put(11)
    MyPQ.put(31)
    MyPQ.put(24)

    print "Max is: ", MyPQ.peek()
    print "Delete max: ", MyPQ.get()
    print "Size: ", MyPQ.size()

if __name__ == '__main__':
    main()
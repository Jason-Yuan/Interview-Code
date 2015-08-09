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

	def insert(self, data):
		"""add a new item to the maxheap"""
		self.maxheap.append(data)
		self.currentSize += 1
		#compare bottom-up
		i = self.currentSize
		# // means devide by 2 and return int
		while i // 2 > 0:
			if self.maxheap[i] > self.maxheap[i // 2]:
				self.maxheap[i], self.maxheap[i // 2] = self.maxheap[i // 2], self.maxheap[i]
			i = i // 2

	def findMax(self):
		"""returns the item with the maxmum key value"""
		return self.maxheap[1]

	def delMax(self):
		"""returns the item with the maxmum key value, removing the item from the heap"""
		res = self.maxheap[1]
		self.maxheap[1] = self.maxheap[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.maxheap.pop()
		self.maxHeapify(self.maxheap, 1)
		return res

	def maxHeapify(self, L, index):
		"""correct single violation in a sub-tree"""
		if index > self.currentSize // 2:
			return
		# find the max child of current index
		if index*2+1 > self.currentSize or L[index*2] > L[index*2+1]:
			maxChild = index*2
		else:
			maxChild = index*2+1
		if L[index] < L[maxChild]:
			L[index], L[maxChild] = L[maxChild], L[index]
		self.maxHeapify(L, index*2)
		self.maxHeapify(L, index*2+1)

	def buildMaxHeap(self, L):
		"""build a new maxheap from an unordered array"""
		self.currentSize = len(L)
		self.maxheap = [0] + L
		for i in range(len(L)//2, 0, -1):
			self.maxHeapify(self.maxheap, i)

	def show(self):
		print self.maxheap[1:]

	def isEmpty(self):
		return self.currentSize == 0

##############################################################################################################################

def main():
	MyPQ = PriorityQueue()
	L = [6, 5, 7, 2, 1, 3, 8]

	MyPQ.buildMaxHeap(L)
	print "Build a priority queue from a list L: ", L
	MyPQ.show()

	MyPQ.insert(15)
	MyPQ.insert(11)
	MyPQ.insert(31)
	MyPQ.insert(24)
	MyPQ.show()

	print "Delete the max: ", MyPQ.delMax()
	MyPQ.show()

if __name__ == '__main__':
	main()
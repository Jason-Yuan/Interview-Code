##############################################################################################################################
#      Project:                  Priority Queue
#      Info:                     1. Priority Queue is implemented based on heap data structure
#                                2. A heap data structure is a array which visualized as NEARLY completed binary tree
#                                3. NEARLY - because the outer(last) layer may not be completed
#                                4. Two types of heap: MinHeap and MaxHeap
##############################################################################################################################

class PriorityQueue:
	def __init__(self):
		self.pq = []
		self.currentSize = 0

	def insert(self, data):
		self.pq.append(data)
		self.currentSize += 1

		#compare bottom-up
		i = self.currentSize
		while i // 2 > 0:
			if self.pq[i-1] > self.pq[(i // 2)-1]:
				self.pq[i-1], self.pq[(i // 2)-1] = self.pq[(i // 2)-1], self.pq[i-1]
			i = i // 2

	def findMax(self):
		return self.pq[0]

	def delMax(self):
		res = self.pq[0]
		self.pq[0] = self.pq[self.currentSize-1]
		self.currentSize = self.currentSize - 1
		self.pq.pop()
		i = 1
		while (i < self.currentSize // 2):
			if self.pq[(i*2)] < self.pq[(i*2)-1]:
				maxChild = (i*2)-1
			else:
				maxChild = i*2
			if self.pq[i-1] < self.pq[maxChild]:
				 self.pq[i-1], self.pq[maxChild] = self.pq[maxChild], self.pq[i-1]
			i *= 2
		return res

	# maxHeapify will correct single violation in a sub-tree
	def maxHeapify(self, L, index):
		if index + 1 > len(L) / 2:
			return
		if L[(index+1)*2] < L[(index+1)*2-1]:
			maxChild = (index+1)*2-1
		else:
			maxChild = (index+1)*2
		L[index], L[maxChild] = L[maxChild], L[index]
		self.maxHeapify(L, (index+1)*2-1)
		self.maxHeapify(L, (index+1)*2)

	# buildMaxHeap will produce a maxheap from an unordered array
	def buildMaxHeap(self, L):
		for i in range(len(L)/2, 0, -1):
			self.maxHeapify(L, i-1)
		self.pq = L
		self.currentSize = len(L)

	def show(self):
		print self.pq

##############################################################################################################################

def main():
	priorityQ = PriorityQueue()
	L = [5, 7, 3, 2, 1, 6, 8]

	priorityQ.buildMaxHeap(L)
	priorityQ.show()

	priorityQ.insert(5)
	priorityQ.insert(15)
	priorityQ.insert(51)
	priorityQ.show()

	print "Delete the max: ", priorityQ.delMax()
	priorityQ.show()

if __name__ == '__main__':
	main()
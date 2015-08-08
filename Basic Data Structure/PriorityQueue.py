# ##############################################################################################################################
# #      Project:                  Priority Queue
# #      Info:                     1. Priority Queue is implemented based on heap data structure
# #                                2. A heap data structure is a array which visualized as NEARLY completed binary tree
# #                                3. NEARLY - because the outer(last) layer may not be completed
# #                                4. Two types of heap: MinHeap and MaxHeap
# ##############################################################################################################################

# class PriorityQueue:
# 	def __init__(self):
# 		self.maxheap = [0]
# 		self.currentSize = 0

# 	def insert(self, data):
# 		self.maxheap.append(data)
# 		self.currentSize += 1

# 		#compare bottom-up
# 		i = self.currentSize
# 		# // means devide by 2 and return int
# 		while i // 2 > 0:
# 			if self.maxheap[i] > self.maxheap[i // 2]:
# 				self.maxheap[i], self.maxheap[i // 2] = self.maxheap[i // 2], self.maxheap[i]
# 			i = i // 2

# 	def findMax(self):
# 		return self.maxheap[1]

# 	def delMax(self):
# 		res = self.maxheap[1]
# 		self.maxheap[1] = self.maxheap[self.currentSize]
# 		self.currentSize = self.currentSize - 1
# 		self.maxheap.pop()
# 		i = 1
# 		while (i < self.currentSize // 2):
# 			if self.maxheap[(i*2)] < self.maxheap[(i*2)-1]:
# 				maxChild = (i*2)-1
# 			else:
# 				maxChild = i*2
# 			if self.maxheap[i-1] < self.maxheap[maxChild]:
# 				 self.maxheap[i-1], self.maxheap[maxChild] = self.maxheap[maxChild], self.maxheap[i-1]
# 			i *= 2
# 		return res

# 	# maxHeapify will correct single violation in a sub-tree
# 	def maxHeapify(self, L, index):
# 		if index + 1 > len(L) / 2:
# 			return
# 		if L[(index+1)*2] < L[(index+1)*2-1]:
# 			maxChild = (index+1)*2-1
# 		else:
# 			maxChild = (index+1)*2
# 		L[index], L[maxChild] = L[maxChild], L[index]
# 		self.maxHeapify(L, (index+1)*2-1)
# 		self.maxHeapify(L, (index+1)*2)

# 	# buildMaxHeap will produce a maxheap from an unordered array
# 	def buildMaxHeap(self, L):
# 		self.maxheap = [0] + L
# 		self.currentSize = len(L)
# 		for i in range(len(L)//2, 0, -1):
# 			self.maxHeapify(self.maxheap, i-1)

# 	def show(self):
# 		print self.maxheap

# ##############################################################################################################################

# def main():
# 	priorityQ = PriorityQueue()
# 	L = [5, 7, 3, 2, 1, 6, 8]

# 	priorityQ.buildMaxHeap(L)
# 	priorityQ.show()

# 	priorityQ.insert(5)
# 	priorityQ.insert(15)
# 	priorityQ.insert(51)
# 	priorityQ.show()

# 	print "Delete the max: ", priorityQ.delMax()
# 	priorityQ.show()

# if __name__ == '__main__':
# 	main()

for i in range(10, 1, -1):
	print i
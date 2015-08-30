##############################################################################################################################
#      Project:                  Heap Sort
#      Time Complexity:          O(nlogn)
#      Space Complexity:         O(1)
#      Stability:                Not stable
##############################################################################################################################

def maxHeapify(L, index):
	"""correct single violation in a sub-tree"""
	if index + 1 > len(L) // 2:
		return
	# find the max child of current index
	if (index+1)*2 > len(L) - 1 or L[(index+1)*2-1] > L[(index+1)*2]:
		maxChild = (index+1)*2-1
	else:
		maxChild = (index+1)*2

	if L[index] < L[maxChild]:
		L[index], L[maxChild] = L[maxChild], L[index]
	maxHeapify(L, (index+1)*2)
	maxHeapify(L, (index+1)*2-1)

def buildMaxHeap(L):
	"""build a new maxheap from an unordered array"""
	for i in range(len(L)//2, 0, -1):
		maxHeapify(L, i-1)

def delMax(L):
	"""returns the item with the maxmum key value, removing the item from the heap"""
	res = L[0]
	L[0] = L[len(L)-1]
	L.pop()
	return res

def HeapSort(L):
	"""sort an unordered array by binary heap"""
	if len(L) < 2:
		return
	res = []
	for i in range(len(L)):
		buildMaxHeap(L)
		res.append(delMax(L))
	L += res

##############################################################################################################################

def main():
	L = [1, 4, 6, 2, 5, 3, 9, 7, 8]
	print "The unordered list is: ", L
	HeapSort(L)
	print "After heap sort: ", L

if __name__ == '__main__':
	main()
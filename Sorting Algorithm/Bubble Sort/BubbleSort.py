#=============================================================================================================================
#      Project:                  Bubble Sort
#      Time Complexity:          O(n2)
#      Space Complexity:         O(1)
#      Stability:                Stable
#=============================================================================================================================

# Basic Bubble Sort
def BubbleSort(L):
	for unsorted in range(len(L)-1, 0, -1):
		for i in range(unsorted):
			if L[i] > L[i+1]:
				L[i], L[i+1] = L[i+1], L[i]


# Bubble Sort with flag to indicate the index after which the array has been sorted
def BubbleSort2(L):
	flag = len(L)-1
	while flag > 0:
		origin_flag = flag
		for i in range(0,origin_flag):
			if L[i] > L[i+1]:
				flag = i
				L[i], L[i+1] = L[i+1], L[i]
		if flag == origin_flag:
			flag = 0



L1 = [2, 3, 5, 1, 7, 6, 8, 9, 10, 4]
L2 = [2, 3, 5, 1, 7, 6, 8, 9, 10, 4]

BubbleSort(L1)
print "BubbleSort: ", L1

BubbleSort2(L2)
print "BubbleSort2: ", L2
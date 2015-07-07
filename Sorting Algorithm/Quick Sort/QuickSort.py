##############################################################################################################################
#      Project:                  Quick Sort
#      Time Complexity:          Expected O(nlogn) / Worst case O(n2)  
#      Space Complexity:         O(n)
#      Stability:                Not stable
#      Info:                     1. It follows the decrease-by-half pattern, so bears some resemblance to merge sort.
#                                2. In quick sort algorithm, a pivot is an element of L used to divide L into three sub_lists.
#                                3. We hope the division process can divide L into two sub-lists of "roughly equal size".
##############################################################################################################################

# First method, deterministic quick sort 
# worst-case time complextity is O(n2)
def Deterministic_QuickSort(L):
	if len(L) <= 1:
		return L
	else:
		pivot = L[0]
		LT = []  # LT means "less than pivot"
		EQ = []  # EQ means "equal to pivot"
		GT = []  # GT means "greater than pivot"
		for x in L:
			if x < pivot:
				LT.append(x)
			elif x == pivot:
				EQ.append(x)
			else:
				GT.append(x)
		LT_S = Deterministic_QuickSort(LT)
		GT_S = Deterministic_QuickSort(GT)
		return LT_S + EQ + GT_S

##############################################################################################################################

# Second method, randomized quick sort, we need to use the random library
# Try to make O(n2)-time scenario less likely to occur.
import random

def Randomized_QuickSort(L):
	if len(L) <= 1:
		return L
	else:
		# for the pivot, we randomly choosed from L, instead of L[0]
		pivot = random.choice(L)
		LT = []
		EQ = []
		GT = []
		for x in L:
			if x < pivot:
				LT.append(x)
			elif x == pivot:
				EQ.append(x)
			else:
				GT.append(x)
		LT_S = Randomized_QuickSort(LT)
		GT_S = Randomized_QuickSort(GT)
		return LT_S + EQ + GT_S

##############################################################################################################################

# Third method, in-place quick sort
# Try to avoid the cost of allocating fresh data structures to store its output.

def Inplace_QuickSort(L):
	Inplace_QuickSort_Range(L, 0, len(L))
	return L

def Inplace_QuickSort_Range(L, s, e):
	if (e - s) > 1:
		lt_end, gt_start = Inplace_Partition(L, s, e)
		Inplace_QuickSort_Range(L, s, lt_end)
		Inplace_QuickSort_Range(L, gt_start, e)

def Inplace_Partition(L, s, e):
	pivot = L[random.randint(s, e-1)]

	# first pass: partition L into LT, GE zones
	lt_end = s
	ge_start = e
	while lt_end < ge_start:
		if L[lt_end] < pivot:
			lt_end += 1
		elif L[ge_start-1] >= pivot:
			ge_start -= 1
		else:
			Swap(L, lt_end, ge_start-1)
			lt_end += 1
	# second pass: partition GE into EQ, GT zones
	eq_end = lt_end
	gt_start = e
	while eq_end < gt_start:
		if L[eq_end] == pivot:
			eq_end += 1
		elif L[gt_start-1] > pivot:
			gt_start -= 1
		else:
			Swap(L, eq_end, gt_start-1)
			eq_end += 1
	return lt_end, gt_start

def Swap(L, i, j):
	L[i], L[j] = L[j], L[i]

##############################################################################################################################

if __name__ == '__main__':
	L1 = [2, 3, 6, 7, 4, 5, 1, 9, 8]
	print ( "Deterministic quick sort: ", Deterministic_QuickSort(L1) )

	L2 = [2, 3, 6, 7, 4, 5, 1, 9, 8]
	print ( "Randomized quick sort: ", Randomized_QuickSort(L2) )

	L3 = [2, 3, 6, 7, 4, 5, 1, 9, 8]
	print ( "Inplace quick sort: ", Inplace_QuickSort(L3) )





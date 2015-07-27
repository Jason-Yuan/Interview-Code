##############################################################################################################################
#      Project:                  Binary Search (relies on sorted list)
#      Time Complexity:          O(n) / O(logn)
#      Space Complexity:         O(1)
#      Stability:                Unstable
#      Info:                     Decrease-by-half searching
##############################################################################################################################

# Method 1 for Binary Search    O(n)
def Binary_search1(L, x):
	n = len(L)
	if n == 0:
		return None
	elif n == 1:
		if L[0] == x:
			return 0
		else:
			return None
	else:
		half = int(n/2)
		A = L[:half]
		B = L[half:]
		if x == L[half]:
			return half
		elif x < L[half]:
			return Binary_search1(A, x)
		else:
			i = Binary_search1(B, x)
			if i is None:
				return None
			else:
				return (half + i)

###################################################################################################

# Method 2 for Binary Search O(logn)
# We do not copy the list into two sublist anymore
def Binary_range(L, x, start, end):
	n = end - start
	if n == 0:
		return None
	elif n == 1:
		if L[start] == x:
			return start
		else:
			return None
	else:
		mid = (start + end)//2 
		if L[mid] == x:
			return mid
		elif L[mid] > x:
			return Binary_range(L, x, start, mid)
		else:
			return Binary_range(L, x, mid+1, end)

def Binary_search2(L, x):
	return Binary_range(L, x, 0, len(L))

###################################################################################################

def main():
	L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	print "Find 9 in the list by method 1: ", Binary_search1(L, 9)
	print "Find 9 in the list by method 2: ", Binary_search2(L, 9)

if __name__ == '__main__':
	main()
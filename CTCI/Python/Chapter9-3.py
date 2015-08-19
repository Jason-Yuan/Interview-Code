##############################################################################################################################
# Ideas: Similarly Binary Search
# Time Complexity: O(logn) 
# Time Complexity for Follow Up: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def findMagicRecur(L, start, end):
	"""Return the magic index, or -1 if it does not exist."""
	if start < 0 or end >= len(L) or start > end:
		return -1
	mid = (start + end) / 2
	if L[mid] == mid:
		return mid
	elif L[mid] > mid:
		return findMagicRecur(L, start, mid-1)
	else:
		return findMagicRecur(L, mid+1, end)

def findMagic(L):
	return findMagicRecur(L, 0, len(L) - 1)

# Follow up, with array that is not distinct integer
def findMagicFollowUpRecur(L, start, end):
	"""Return the magic index, or -1 if it does not exist."""
	if start < 0 or end >= len(L) or start > end:
		return -1
	mid = (start + end) / 2
	if L[mid] == mid:
		return mid
	left_end = min(L[mid], mid - 1)
	left = findMagicFollowUpRecur(L, start, left_end)
	if left >= 0:
		return left
	right_start = max(L[mid], mid + 1)
	right = findMagicFollowUpRecur(L, right_start, end)
	return right

def findMagicFollowUp(L):
	return findMagicFollowUpRecur(L, 0, len(L) - 1)

##############################################################################################################################

def main():
	a = [-40, -1, 1, 2, 3, 5, 7, 9, 12, 13]
	b = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
	print "Array is: ", a
	print "The magic index is: ", findMagic(a)
	print "Follow Up"
	print "Array is:", b
	print "The magic index is: ", findMagicFollowUp(b)

if __name__ == '__main__':
	main()
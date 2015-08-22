##############################################################################################################################
# Ideas:	1. First to clearify, one rotate means move a large number from last to first eg 123456 -> 612345 -> 561234
#       	2. Compare with the binary search we need to consider about the list[mid] sit in large part or small part
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
##############################################################################################################################

def searchRotate(L, target):
	start = 0
	end = len(L) - 1
	while  start <= end:
		mid = (start + end) / 2
		if L[mid] == target:
			return mid
		if L[mid] >= L[start]:
			if target > L[start] and target < L[mid]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			if target > L[mid] and target < L[start]:
				start = mid + 1
			else:
				end = mid - 1

	return -1

##############################################################################################################################

def main():
	a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	target = 25
	print "Find {} in {} \nPosition is {}".format(target, a, searchRotate(a, target))

if __name__ == '__main__':
	main()
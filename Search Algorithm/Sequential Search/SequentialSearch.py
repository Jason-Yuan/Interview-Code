##############################################################################################################################
#      Project:                  Sequential Search (Linear Search)
#      Time Complexity:          O(n) / Best Case O(1)
#      Space Complexity:         O(1)
#      Stability:                Unstable
#      Info:                     Decrease-by-one searching
##############################################################################################################################

def SequentialSearch(L, value):
	"""If found the value return position, else return false"""
	pos = 0
	for e in L:
		if e == value:
			return pos
		pos +=1

	return False

##############################################################################################################################

def main():
	L = [1, 2, 5, 6, 7, 9]
	print "Trying to find 6 in list L"
	print "Sequential Search result is: ", SequentialSearch(L, 6)

if __name__ == '__main__':
	main()
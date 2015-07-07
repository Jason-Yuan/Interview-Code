###################################################################################################
# Method 1
# Ideas: Assume we have 256 ASCII characters, we set up a array of 256 flags. Iterate each char in 
#        the given string, first convert it to value of the byte(e.g. 97), then check if the flag 
#        of array[97] is true, turn it to false, if the flag of array[97] is false, return false.
# Time Complexity: O(n)
# Space Complexity: O(1)
# FYI: ord() is a build-in method which is the inverse of chr() for 8-bit strings(e.g. ord('a') = 97)
###################################################################################################

def isAllUniqueChar(s):
	"return true if a string only contains unique characters"

	# if a stirng is longer than 256 or is None, return false
	if s is None or len(s) > 256:
		return False

	Flag = [True for i in range(256)]
	for char in s:
		index = ord(char) # if you consider the Flag as a hash table, ord() should be the hash function
		if Flag[index]:
			Flag[index] = False
		else:
			return False

	return True 


###################################################################################################
# Method 2
# Ideas: First, sort the stirng, if there are duplicates in the given string, they should be 
#        neighbor then. Iterate each element in the stirng to see if the neighbors are same.
# Time Complexity: O(nlgon) base on the sort algorithm - e.g. quick sort
# Space Complexity: O(1)
###################################################################################################

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

def isAllUniqueChar2(s):
	"return true if a string only contains unique characters"

	# if a stirng is longer than 256 or is None, return false
	if s is None or len(s) > 256:
		return False

	sortedStr = Randomized_QuickSort(s)
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False

	return True

###################################################################################################

if __name__ == "__main__":
	s = "Hello, World"
	print "Method 1: ", isAllUniqueChar(s)
	print "Method 2: ", isAllUniqueChar2(s)





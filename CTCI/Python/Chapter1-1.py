###################################################################################################
# Method 1
# Ideas: Assume we have 256 ASCII characters, we set up a array of 256 flags. Iterate each char in the given string, first convert it to value of the byte(e.g. 97), then check if the flag of array[97] is true, turn it to false, if the flag of array[97] is false, return false
# Time Complexity: O(n)
# Space Complexity: O(1)
# FYI: ord() is a build-in method which is the inverse of chr() for 8-bit strings(e.g. ord('a') = 97)

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
# Ideas: First, sort the stirng, if there are duplicates in the given string, they should be neighbor then. Iterate each element in the stirng to see if the neighbors are same
# Time Complexity: O(nlgon) base on the sort algorithm - e.g. quick sort
# Space Complexity: O(1)
# FYI: the example below just use the build-in sorted() method

def isAllUniqueChar(s):
	"return true if a string only contains unique characters"

	# if a stirng is longer than 256 or is None, return false
	if s is None or len(s) > 256:
		return False

	sortedStr = sorted(s)
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False

	return True
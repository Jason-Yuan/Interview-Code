##############################################################################################################################
# Method 1
# Ideas: For both of the them, for example, we can sort them with MergeSort, and then compare them.
# Time Complexity: O(nlogn) based on the sorting algorithm
# Space Complexity: O(1)
##############################################################################################################################

# start define merge sort

def Merge(A, B):
	S = ""
	ai = 0
	bi = 0
	while len(A) > ai and len(B) > bi:
		if A[ai] <= B[bi]:
			x = A[ai]
			ai += 1
		else:
			x = B[bi]
			bi += 1
		S += x
	return S + A[ai:] + B[bi:]

def MergeSort(L):
	if len(L) <= 1:
		return L
	else:
		half = int(len(L) / 2)
		A = L[:half]
		B = L[half:]
		return Merge(MergeSort(A), MergeSort(B))

# end define merge sort

def IsPermutation1(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		sorted_s1 = MergeSort(s1)
		sorrted_s2 = MergeSort(s2)

		if sorted_s1 == sorrted_s2:
			return True
		else:
			return False

##############################################################################################################################
# Method 2
# Ideas: First create a flag array of 256 ZERO, since there are only 256 different ASCII characters.
#        Then, for each of the char in string_1 map to the array, flag++
#        And, for each of the char in string_2 map to the array, flag--
#        If all elements in the array still 0, then string_2 is the permutation of string_1
# Time Complexity: O(n) 
# Space Complexity: O(1)
##############################################################################################################################

def IsPermutation2(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		Flag = [0 for i in range(256)]
		for x in s1:
			Flag[ord(x)] +=1

		for x in s2:
			Flag[ord(x)] -=1

	for f in Flag:
		if f != 0:
			return False

	return True

##############################################################################################################################

def main():
	string1 = "Hello,World!"
	string2 = "oHell,!Wordl"
	print "Is \"{}\" a permutation of \"{}\"".format(string2, string1)
	print "Result 1: ", IsPermutation1(string1, string2)
	print "Result 2: ", IsPermutation2(string1, string2)

if __name__ == '__main__':
	main()

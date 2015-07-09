##############################################################################################################################
# Ideas: For both of the them, for example, we can sort them with MergeSort, and then compare them.
# Time Complexity: O(nlogn)
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

def isPermutation(s1, s2):
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

def main():
	string1 = "Hello,World!"
	string2 = "oHell,!Wordl"
	print "Is \"{}\" a permutation of \"{}\"".format(string2, string1)
	print "Result is: ", isPermutation(string1, string2)

if __name__ == '__main__':
	main()

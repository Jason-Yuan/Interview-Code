##############################################################################################################################
# Ideas: Compare from the last element of A and B
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def mergeArray(A, B):
	if B is None or len(B) == 0:
		return A
	lastA = len(A) - 1
	lastB = len(B) - 1
	A += [None for i in range(len(B))]
	end = len(A) - 1
	while lastB >= 0 and lastA >= 0:
		if B[lastB] >= A[lastA]:
			A[end] = B[lastB]
			end -= 1
			lastB -= 1
		else:
			A[end] = A[lastA]
			end -= 1
			lastA -=1

	if lastA < 0:
		while lastB != 0:
			A[end] = B[lastB]
			lastB -= 1

##############################################################################################################################

def main():
	a = [1, 3, 5]
	b = [2, 4, 6]
	mergeArray(a, b)
	print a

if __name__ == '__main__':
	main()
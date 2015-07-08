##############################################################################################################################
#      Project:                  Insertion Sort
#      Time Complexity:          O(n2)  
#      Space Complexity:         O(1)
#      Stability:                Stable
#      Info:                     Decrease-by-one sorting
##############################################################################################################################

# In-place insertion sort
def Inplace_InsertionSort(L):
	for i in range(1,len(L)):  # we assume L[0] is the sorted sublist
		currentvalue = L[i]

		while i > 0 and L[i-1] > currentvalue:
			L[i]=L[i-1]
			i -= 1

		L[i] = currentvalue


##############################################################################################################################

def main():
	L = [1, 4, 3, 5, 6, 2]
	Inplace_InsertionSort(L)
	print "Inplace InsertionSort: ", L

if __name__ == '__main__':
	main()
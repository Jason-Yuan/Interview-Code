##############################################################################################################################
# Ideas: Iterative building larger subset based on small subsets, adding new elem in.
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
##############################################################################################################################

def subset(L):
	result = [[]]
	for x in L:
		with_x = []
		for res in result:
			with_x.append(res + [x])
		result += with_x
	return result

##############################################################################################################################

def main():
	l = [1, 2, 3]
	print "The list is:", l
	print "The subsets are:", subset(l)  

if __name__ == '__main__':
	main()
##############################################################################################################################
# Ideas:	0 comes from 5 *  2, and since frequency of 2 is higher than 5, so we just count 5
#        	5!  ----- 1 -> 5
#			10! ----- 2 -> 5
#			15! ----- 3 -> 5
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def findZeros(n):
	if not n:
		return -1

	i, count = 5, 0
	while n / i > 0:
		count += n / i
		i *= 5
	
	return count

##############################################################################################################################

def main():
	m = 20
	n = 100
	print "Number of zeros for factorial of {} is {}".format(m, findZeros(m))
	print "Number of zeros for factorial of {} is {}".format(n, findZeros(n))

if __name__ == '__main__':
		main()	
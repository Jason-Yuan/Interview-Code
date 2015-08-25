##############################################################################################################################
# Ideas:	if (a - b) < 0 k = 1 else k = 0 return a - k * (a - b)
#           if a > b then (a - b) > 0 first bit = 0 else first bit = 1
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def max1(a, b):
	sign = a - b
	sign = (sign >> 1) & 1
	return a - sign * (a - b)

def max2(a, b):
	res = [a, b]
	index = a - b
	index = (index >> 31) & 1
	return res[index]

##############################################################################################################################

def main():
	a = 10
	b = 5
	print "The max number of ({}, {}) is {}".format(a, b, max1(a, b))
	print "The max number of ({}, {}) is {}".format(a, b, max2(a, b))

if __name__ == '__main__':
	main()
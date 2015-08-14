##############################################################################################################################
# Ideas: if a number a is power of 2, that means its binary representation only has one "1"
#        so, a & (n - 1) should equal to 0
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def isPowerOf2(num):
	if num == 0:
		return False
	if (num & num - 1) == 0:
		return True
	else:
		return False

##############################################################################################################################

def main():
	print "Is {0} power of 2? {1}".format(14, isPowerOf2(14))
	print "Is {0} power of 2? {1}".format(1, isPowerOf2(1))
	print "Is {0} power of 2? {1}".format(0, isPowerOf2(0))
	print "Is {0} power of 2? {1}".format(256, isPowerOf2(256))

if __name__ == '__main__':
	main()
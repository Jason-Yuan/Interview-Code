##############################################################################################################################
# Ideas: first a ^ b, then calculate how many 1 are there 
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def bitSwapRequired(a, b):
	temp = a ^ b
	if temp == 0:
		return 0
	n = 1
	while (temp != 0) and (temp & (temp - 1) > 0):
		n += 1
		temp = temp & (temp - 1)
	return n

##############################################################################################################################

def main():
	a = 0b1100110101011
	b = 0b1011010101010

	print "How many bit need to be swaped? ", bitSwapRequired(a, b)

if __name__ == '__main__':
		main()	
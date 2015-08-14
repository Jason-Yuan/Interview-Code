##############################################################################################################################
# Ideas: 1. getNext() find the rightmost "01" change to "10", and put all the "1" 
#                     at the right of "01" all the way to the right
#                     e.g.   01 111000 => 10 000111
#        2. getPrev() find the rightmost "10" change to "01", and put all the "1"
#                     at the right of "10" all the way to the left
#                     e.g.   10 000011 => 01 110000
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def getNext(num):
	c = num
	c0 = 0
	c1 = 0
	# calculate c0 and c1
	while (((c & 1) == 0) and (c != 0)):
		c0 += 1
		c >>= 1

	while ((c & 1) == 1):
		c1 += 1
		c >>= 1

	# if 000000000 or 11111000000 return Error
	if c0 + c1 == 32 or c0 + c1 == 0:
		return -1

	# get position of 0 of the rightmost "01"
	p = c0 + c1

	num |= (1 << p) # change "01" to "11"
	num &= ~((1 << p) - 1) # clear all bits right of p, set to 0
	num |= (1 << (c1 -1)) - 1
	# for line 32 to 34, we can use arithmetical way
	# num = num + (1 << c0) + (1 << (c1 -1)) - 1

	return num

def getPrev(num):
	c = num
	c0 = 0
	c1 = 0
	# calculate c0 and c1
	while ((c & 1) == 1):
		c1 += 1
		c >>= 1
	
	# if 000000000 or 000001111111 return Error
	if c == 0:
		return -1

	while (((c & 1) == 0) and (c != 0)):
		c0 += 1
		c >>= 1

	# get position of 0 of the rightmost "10"
	p = c0 + c1

	num &= (~0 << (p + 1)) # change "10...." to "0000000000"
	mask = (1 << (c1 + 1)) - 1 # get c1+1 ones "1111"
	num |= mask << (c0 -1)

	return num

##############################################################################################################################

def main():
	print "Next Smallest: {0:b} => {1:b}".format(44, getNext(44))
	print "Next Smallest: {0:b} => {1:b}".format(142, getNext(142))
	print "Prev Largest: {0:b} => {1:b}".format(91, getPrev(91))
	print "Prev Largest: {0:b} => {1:b}".format(307, getPrev(307))

if __name__ == '__main__':
		main()	
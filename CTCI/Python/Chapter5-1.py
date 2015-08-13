##############################################################################################################################
# Bit Manipulations:
#                    >>    			# Right Shift
# 					 <<    			# Left Shift
# 					 &     			# Bitwise AND
# 					 |     			# Bitwise OR
# 					 ^     			# Bitwise XOR
# 					 ~x    			# Bitwise NOT, returns complement of x which equals -x-1
#                    bin(5)			# output 0b101
#                    hex(15)        # output 0xf
#					 int("111",2)   # output 7
#					 int("0b111",2) # output 7
# Ideas:     1. clean n from i to j, set to 0
#            2. shift m i bits
#            3. n_cleaned | m_shifted
##############################################################################################################################
 
def updateBits(n, m, i, j):
	allOnes = ~0
	left = allOnes << (j+1)
	right = (1<<i)-1
	mask = left | right
	n_cleared = n & mask
	m_shifted = m << i
	return n_cleared | m_shifted

##############################################################################################################################

def main():
	a = 0b10000000000
	b = 0b10011
	print "First number is: ", '{0:b}'.format(a)
	print "Second number is: ", '{0:b}'.format(b)
	print '{0:b}'.format(updateBits(a, b, 2, 6))

if __name__ == '__main__':
	main()
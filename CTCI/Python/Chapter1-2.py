##############################################################################################################################
# Ideas: 
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def Reverse(s):
	return s[::-1]

##############################################################################################################################

def main():
	s = "Hello, World!"
	result = Reverse(s)
	print "Before: ", s
	print "After: ", result

if __name__ == '__main__':
	main()
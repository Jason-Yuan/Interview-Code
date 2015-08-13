##############################################################################################################################
# Ideas: keep adding 2^-n and compare to the original number up to 32 times
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def representBinary(num):
	if num > 1 or num < 0:
		return "ERROR"
	res = "0."
	sum = 0
	for i in range(1, 33):
		if sum + pow(2, -i) == num:
			return res + "1"
		elif sum + pow(2, -i) > num:
			res += "0"
		else:
			sum += pow(2, -i)
			res += "1"
	return "an ERROR"

##############################################################################################################################

def main():
	print "Convert 10 to 32-bit binary: ", representBinary(10)
	print "Convert 0.5 to 32-bit binary: ", representBinary(0.5)
	print "Convert 0.125 to 32-bit binary: ", representBinary(0.125)
	print "Convert 0.6418609619140625 to 32-bit binary: ", representBinary(0.6418609619140625)

if __name__ == '__main__':
	main()
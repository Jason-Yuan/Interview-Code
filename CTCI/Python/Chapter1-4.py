##############################################################################################################################
# Method 1
# Ideas: For both of the them, for example, we can sort them with MergeSort, and then compare them.
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def Replace1(s):
	s_list = list(s)
	for i in range(len(s_list)):
		if s_list[i] == " ":
			s_list[i] = '%20'
	return "".join(s_list)

##############################################################################################################################
# Method 2
# Ideas: Make a string called result whose length is equal to the lenght after replace " " with "%20", copy the char from 
#        input string to result, when meet " ", copy "%20"
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

# The second method, just try to implement with the C++ style
def Replace2(s):
	# calculate the number of space contained in input string s
	count_space = 0
	for x in s:
		if x == " ":
			count_space += 1

	# allocate a space for the result string
	result = [" " for i in range(0, len(s) + 2 * count_space)]

	# copy char from left to right 
	j = 0
	for x in s:
		if x != " ":
			result[j] = x
			j += 1
		else:
			result[j] = "%"
			result[j+1] = "2"
			result[j+2] = "0"
			j += 3

	return "".join(result)

##############################################################################################################################

def main():
	string = "Mr John Smith"
	print "Input: ", string
	result1 = Replace1(string)
	result2 = Replace2(string)
	print "Result 1: ", result1
	print "Result 2: ", result2
	print "Result 3: ", string.replace(" ", "%20")

if __name__ == '__main__':
	main()
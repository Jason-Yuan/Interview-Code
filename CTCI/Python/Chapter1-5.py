##############################################################################################################################
# Ideas: Make a new string with the same length, then iterate each char in of the input string.
#        Copy last_char and count to the new string
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def CompressString(s):
	if not s:
		return
	compressed_s = ""
	last_char = s[0]
	count = 1
	for i in range(1,len(s)):
		if s[i] == last_char:
			count += 1
			continue
		else:
			compressed_s += last_char + str(count)
			last_char = s[i]
			count = 1
	compressed_s += last_char + str(count)

	return compressed_s if len(compressed_s) < len(s) else s 

##############################################################################################################################

def main():
	string1 = "aaabcddeeeee"
	string2 = "abc"
	result1 = CompressString(string1)
	result2 = CompressString(string2)
	print "The compressed version of \"{}\" is \"{}\"".format(string1, result1)
	print "The compressed version of \"{}\" is \"{}\"".format(string2, result2)

if __name__ == '__main__':
	main()
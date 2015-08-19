##############################################################################################################################
# Ideas: Recursion, eg for "abc"
#                   permutaion(abc) ==> a + permutation(bc) ===> a + b + permutation(c)
#                                                           ===> a + c + permutation(b)
#                                       b + permutation(ac) ===> b + a + permutation(c)
#                                                           ===> b + c + permutation(a)
#                                       c + permutation(ab) ===> c + a + permutation(b)
#                                                           ===> c + b + permutation(a)  
# Time Complexity: O(n!)
# Space Complexity: O(n!)
##############################################################################################################################

def permutation(str):
	if str == "":
		return [""]

	res = []
	for i in range(len(str)):
		temp = permutation(str[:i] + str[i+1:])
		for substr in temp:
			res.append(str[i] + substr)
	return res

##############################################################################################################################
# Method 2
# Ideas:                  initial  []
#                                  [a]
#                       [ab]               [ba]
#                [cab] [acb] [abc]   [cba] [bca] [bac]
# Time Complexity: O(n^3 * n!)
# Space Complexity: O(n * n!)
##############################################################################################################################

def permutation2(str):
	result = [ [] ]
	for x in str:
		extended = []
		for s in result:
			for k in range(len(s)+1):
				extended.append(s[:k] + [x] + s[k:])
		result = extended
	return result

##############################################################################################################################

def main():
	a = "abc"
	print "Method 1, permutaion of \"{}\" is {}".format(a, permutation(a))
	print "Method 2, permutaion of \"{}\" is {}".format(a, permutation2(a))

if __name__ == '__main__':
	main()
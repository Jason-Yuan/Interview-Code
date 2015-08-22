##############################################################################################################################
# Ideas:	1. sortStr() will turn "bacd" to "abcd"
#       	2. iterate the item in the array and hash them to a hashmap, "yes", "eys" "sye" will go to the same list
#           3. go through the hashmap and append each item to the return array
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################
 
def sordStr(str):
	return "".join(sorted(str))

def groupByAnagrams(L):
	hashmap = {}
	for word in L:
		if sordStr(word) in hashmap:
			hashmap[sordStr(word)].append(word)
		else:
			hashmap[sordStr(word)] = [word]

	res = []
	for key, value in hashmap.iteritems():
		for word in value:
			res.append(word)

	return res

##############################################################################################################################

def main():
	a = ["axyz", "abc", "yzax", "bac", "zyxa", "fg", "gf"]
	print "The original array is: {}".format(a)
	print "Sorted by anagrams: {}".format(groupByAnagrams(a))

if __name__ == '__main__':
	main()
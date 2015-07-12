##############################################################################################################################
#      Project:                  Brute Force Algorithm
#      Time Complexity:          O(n*m)  
#      Stability:                Stable
#      Info:                     BM algorithm use two lookup table for "Bad Character" and "Good Suffix" rules
#                                BMH(Boyer-Moore-Horspool) algorithm only use "Bad Character" rule
#                                Reference: 1. http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html
#                                           2. https://www.youtube.com/watch?v=Wj606N0IAsw
##############################################################################################################################

def IsSubtring(string, pattern):
	for i in range(len(string)-len(pattern)+1):
		result = True
		for j in range(len(pattern)):
			if pattern[j] != string[i+j]:
				result = False
		if result:
			return True
	return False

##############################################################################################################################

def main():
	text = "This is an example for finding substring."
	word = "example"
	print "Text: ", text
	print "Word: ", word
	print "Does the text contain the word? ", IsSubtring(text, word)

if __name__ == '__main__':
	main()
##############################################################################################################################
#      Project:                  Boyer Moore string Search Algorithm
#      Time Complexity:          Best case: O(n/m)  /  Worst case: O(n*m)  
#      Stability:                Not stable
#      Info:                     BMH(Boyer-Moore-Horspool) algorithm only use "Bad Character" rule
#                                Reference: 1. http://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html
#                                           2. https://www.youtube.com/watch?v=Wj606N0IAsw
##############################################################################################################################

def BMHSearch(haystack, needle):
    # m = len(needle)
    # n = len(haystack)
    Index = []
    if len(needle) > len(haystack):
        return Index
    # construct the bad-character table
    BadCharTable = []
    for i in range(256):
        BadCharTable.append(len(needle))
    for i in range(len(needle) - 1):
        BadCharTable[ord(needle[i])] = len(needle) - i - 1

    # Make the BadCharTable immutable
    BadCharTable = tuple(BadCharTable)

    # i will be the index of the haystack (outer loop)
    # j will be the index of the needle (inner loop)
    i = len(needle) - 1
    
    # while the outer loop hasn't arrived at the end of the haystack
    while i < len(haystack):
        j = len(needle)
        # while the inner loop hasn't arrived at the front of the needle and the compared characters are equal
        while j > 0 and needle[j - 1] == haystack[i + j - len(needle)]:
            j -= 1
        # success, keep a record in the result Index
        if j == 0:
        	Index.append(i + j - len(needle) + 1)
        # For each time we assume the last char is bad-char, and search the BadCharTable for skip steps
        i += BadCharTable[ord(haystack[i])]  

    return Index

##############################################################################################################################

def main():
	haystack = "This is a test for finding substring in a text!"
	needle = " te"

	print "Find \"{}\" from the below sentence.".format(needle)
	print haystack
	print "Result index is: ", BMHSearch(haystack, needle)

if __name__ == '__main__':
	main()
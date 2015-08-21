##############################################################################################################################
# Ideas: Recursion with memorization
#        Dynamic Programing
#        Use cache = {} as a hash map
# Time Complexity: O(n!)
# Space Complexity: O(n)
##############################################################################################################################

def parenthesizeCount(exp, boolean, cache = {}):
	if len(exp) == 1:
		exp = int(exp[0])
		if exp == 1 and boolean:
			return 1
		if exp == 0 and not boolean:
			return 1
		return 0
	if exp in cache:
		return cache[exp]
	else:
		c = 0
		if boolean:
			for i in range(1, len(exp), 2):
				op = exp[i]
				if op == "^":
					c += parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], False, cache) + \
				    	 parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i+1:], True, cache)
				elif op == "|":
					c += parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], True, cache) +\
				    	 parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i+1:], True, cache) +\
				   		 parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], False, cache)
				elif op == "&":
					c += parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], True, cache)
		else:
			for i in range(1, len(exp), 2):
				op = exp[i]
				if op == "^":
					c += parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], True, cache) + \
				    	 parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i+1:], False, cache)
				elif op == "&":
					c += parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i+1:], False, cache) +\
				    	 parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i+1:], True, cache) +\
				   		 parenthesizeCount(exp[:i], True, cache) * parenthesizeCount(exp[i+1:], False, cache)
				elif op == "|":
					c += parenthesizeCount(exp[:i], False, cache) * parenthesizeCount(exp[i:], False, cache) 
		cache[exp] = c
		return c

##############################################################################################################################

def main():
	expression1 = "1^0|0|0|1"
	expression2 = "1&0|0|0&0^0"
	boolean = True
	print "For expression \"{}\" and boolean {}, the number of ways of parenthesizing is {}".format(expression1, str(boolean), parenthesizeCount(expression1, boolean))
	print "For expression \"{}\" and boolean {}, the number of ways of parenthesizing is {}".format(expression2, str(boolean), parenthesizeCount(expression2, boolean))

if __name__ == '__main__':
	main()
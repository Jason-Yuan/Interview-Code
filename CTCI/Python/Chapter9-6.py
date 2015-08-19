##############################################################################################################################
# Method 1
# Ideas: Recursion 
# Time Complexity: O(?)
# Space Complexity: O(?)
##############################################################################################################################

def parentheses(n):
	if n == 1:
		return ["()"]
	res = []
	for p in parentheses(n - 1):
		p1 = "(){}".format(p)
		p2 = "({})".format(p)
		p3 = "{}()".format(p)

		temp = [p1, p2]
		if p1 != p3:
			temp.append(p3)
		res += temp
	return res

##############################################################################################################################
# Method 2
# Ideas: Recursion, DFS 
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
##############################################################################################################################

def parentheses2(n):
	res = []
	parenthesesRecur(res, "", n, n)
	return res

def parenthesesRecur(res, cur, left, right):
	if left == 0 and right == 0:
		res.append(cur)

	if left > 0:
		parenthesesRecur(res, cur + "(", left - 1, right)

	if right > left:
		parenthesesRecur(res, cur + ")", left, right - 1)

##############################################################################################################################

def main():
	n = 3
	print "Valid parentheses for n = {} is {}".format(n, parentheses(n))
	print "Valid parentheses for n = {} is {}".format(n, parentheses2(n))

if __name__ == '__main__':
	main()
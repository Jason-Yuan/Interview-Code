##############################################################################################################################
# Method 1
# Ideas: Recursion
# Time Complexity: O(3^n)
# Space Complexity: O(n)
##############################################################################################################################

def waysToClimb(steps):
	if steps < 0:
		return 0
	elif steps is 0:
		return 1
	else:
		return waysToClimb(steps-1) + waysToClimb(steps-2) + waysToClimb(steps-3)

##############################################################################################################################
# Method 1
# Ideas: Dynamic Programing
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def waysToClimbDP(steps):
	if steps < 0:
		return -1
	T = [None] * (steps+1) 
	for i in range(steps+1):
		if i < 2:
			T[i] = 1
		elif i == 2:
			T[i] = 2
		else:
			T[i] = T[i - 1] + T[i - 2] + T[i - 3]
	return T[steps]

##############################################################################################################################

def main():
	a = 1
	b = 3
	c = 5
	d = 10
	print "For {} stairs, possible ways = {}".format(a, waysToClimb(a))
	print "For {} stairs, possible ways = {}".format(b, waysToClimb(b))
	print "For {} stairs, possible ways = {}".format(c, waysToClimb(c))
	print "For {} stairs, possible ways = {}".format(d, waysToClimb(d))
	print "For {} stairs, possible ways = {}".format(a, waysToClimbDP(a))
	print "For {} stairs, possible ways = {}".format(b, waysToClimbDP(b))
	print "For {} stairs, possible ways = {}".format(c, waysToClimbDP(c))
	print "For {} stairs, possible ways = {}".format(d, waysToClimbDP(d))

if __name__ == '__main__':
	main()
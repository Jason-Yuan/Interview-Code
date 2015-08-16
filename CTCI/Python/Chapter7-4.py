##############################################################################################################################
# Ideas: Firstly implement negate and abs methods
##############################################################################################################################

def negate(x):
	neg = 0
	one = -1 if x > 0 else 1
	while x != 0:
		neg += one
		x += one
	return neg

def abs(val):
	return val if val > 0 else negate(val)

def multiply(x, y):
	if x < y:
		return multiply(y, x)
	res = 0
	i = abs(y)
	while i != 0:
		res += x
		i -= 1
	return res if y  > 0 else negate(res)

def subtract(x, y):
	return x + negate(y)

def divide(x, y):
	if y == 0:
		return "Error"
	absx = abs(x)
	absy = abs(y)
	temp = 0
	quotient = 0
	while temp + absy <= absx:
		temp += absy
		quotient += 1

	return quotient if (x > 0 and y > 0) or (x < 0 and y < 0) else negate(quotient)

##############################################################################################################################

def main():
	a = 10
	b = 5
	c = 0
	d = -12
	print "{} multiply {} equals to {}".format(a, b, multiply(a, b))
	print "{} multiply {} equals to {}".format(a, d, multiply(a, d))
	print "{} subtract {} equals to {}".format(a, b, subtract(a, b))
	print "{} subtract {} equals to {}".format(c, d, subtract(c, d))
	print "{} divide {} equals to {}".format(a, b, divide(a, b))
	print "{} divide {} equals to {}".format(d, b, divide(d, b))

if __name__ == '__main__':
	main()

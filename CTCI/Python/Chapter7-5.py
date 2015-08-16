import math
##############################################################################################################################
# Ideas: 1. The line that cuts two squares in half must connect the two middles
#        2. Remember to handle the special case where x1 == x2 then the slope calculation will throw a divide by 0 exception
##############################################################################################################################
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "{},{}".format(self.x, self.y)

class Line(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end	

	def __str__(self):
		return "Start point is ({}), and end point is ({})".format(self.start, self.end)

class Square(object):
	def __init__(self, left, top, right, bottom):
		self.left = left
		self.top = top
		self.right = right
		self.bottom = bottom
		self.size = math.fabs(left - right)

	def middle(self):
		return Point((self.left + self.right) / 2.0, (self.top + self.bottom) / 2.0)

	def extend(self, mid1, mid2, size):
		xdir = 1 if mid1.x > mid2.x else -1
		ydir = 1 if mid1.y > mid2.y else -1

		# if mid1 and mid2 has same x, then the slope calculation will throw a divide by 0 exception, so compute specially
		if mid1.x == mid2.x:
			return Point(mid1.x, mid1.y + ydir * size / 2.0)

		slope = (mid1.y - mid2.y) / (mid1.x - mid2.x)
		x = 0
		y = 0

		if (math.fabs(slope) == 1):
			x = mid1.x + xdir * size / 2.0
			y = mid1.y + ydir * size / 2.0
		elif (math.fabs(slope) < 1):
			x = mid1.x + xdir * size / 2.0
			y = slope * (x - mid1.x) + mid1.y
		else:
			y = mid1.y + ydir * size / 2.0
			x = (y - mid1.y) / slope + mid1.x
		return Point(x, y)

	def cutInHalf(self, square):
		p1 = self.extend(self.middle(), square.middle(), self.size)
		p2 = self.extend(self.middle(), square.middle(), -1 * self.size)
		p3 = self.extend(square.middle(), self.middle(), self.size)
		p4 = self.extend(square.middle(), self.middle(), -1 * self.size)

		start = p1
		end = p1
		points = [p2, p3, p4]

		for point in points:
			if point.x < start.x or (point.x == start.x and point.y < start.y):
				start = point
			elif point.x > end.x or (point.x == end.x and point.y > end.y):
				end = point

		return Line(start, end)

##############################################################################################################################

def main():
	square1 = Square(1, 3, 3, 1)
	square2 = Square(-5, -1, -3, -3)

	print square1.cutInHalf(square2)
if __name__ == '__main__':
	main()
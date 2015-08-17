import math
import random
##############################################################################################################################
# Ideas: 1. Choose a data structure to represent the line as slope and y-intercept
#        2. For n points, we could draw n^2 lines
#        3. Find the most commom line, using hash table
#        4. Always compare two floating number within a epsilon value instead of == 
##############################################################################################################################

class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({},{})".format(self.x, self.y)

class Line(object):
	def __init__(self, point1, point2):
		self.infinite_slope = False
		self.epsilon = 0.000001
		self.slope = None
		if math.fabs(point1.x - point2.x) > self.epsilon:
			self.slope = (point1.y - point2.y) / float(point1.x - point2.x)
			self.intercept = point1.y - self.slope * point1.x
		else:
			self.infinite_slope = True
			self.intercept = float(point1.x) # x-intercept since slope is infinite

	def isEqual(self, Line):
		if self.infinite_slope != Line.infinite_slope:
			return False
		if self.infinite_slope == True:
			return True
		if math.fabs(self.slope - Line.slope) < self.epsilon and math.fabs(self.intercept - Line.intercept) < self.epsilon:
			return True
		return False

	def hashCode(self):
		return float(int(self.intercept / self.epsilon)) * self.epsilon

	def __str__(self):
		if self.slope:
			return "Line slope is {}, and y-intercept is {}".format(self.slope, self.intercept)
		else:
			return "Line slope is infinite, and x-intercept is {}".format(self.intercept)

def findBestLine(Points):
	Lines = {}
	bestCount = 0
	bestline = None
	for i in range(len(Points)):
		for j in range(i + 1, len(Points)):
			line = Line(Points[i], Points[j])
			key = line.hashCode()
			if key in Lines.keys():
				Lines[key].append(line)
			else:
				Lines[key] = [line]
			count = countEquivalentLines(Lines, line)
			if count > bestCount:
				bestCount = count
				bestline = line
	return bestline

def countEquivalentLines(Lines, line):
	if Lines == None:
		return 0
	key = line.hashCode()
	count = 0
	if key in Lines:
		for l in Lines[key]:
			if l.isEqual(line):
				count += 1
	if (key + line.epsilon) in Lines:
		for l in Lines[key + line.epsilon]:
			if l == line:
				count += 1
	if (key - line.epsilon) in Lines:
		for l in Lines[key - line.epsilon]:
			if l == line:
				count += 1

	return count 

##############################################################################################################################

def main():
	points = []
	for i in range(10):
		x = random.uniform(-10, 10)
		y = random.uniform(-10, 10)
		points.append(Point(x, y))

	for i in range(5):
		points.append(Point(i, i))

	print "Points are: "
	for point in points:
		print point

	print "Best line: ", findBestLine(points)

if __name__ == '__main__':
	main()
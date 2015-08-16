import math
##############################################################################################################################
# Ideas: 1. Better to use a data structure to represent the line
#        2. Do not check float numbers with ==
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

class Line(object):
	__slot__ = {'method_name', 'heuristic_estimate'}

	def __init__(self, slope, yintercept):
		self.epsilon = 0.000001
		self.slope = slope
		self.yintercept = yintercept

	def intersect(self, Line):
		return math.fabs(self.slope - Line.slope) > self.epsilon or \
		       math.fabs(self.yintercept - Line.yintercept) < epsilon

##############################################################################################################################

def main():
	line1 = Line(0.5, 13)
	line2 = Line(0.8, 1)

	print "Is line1 and line2 has intersect? {}".format(line1.intersect(line2))

if __name__ == '__main__':
	main()
##############################################################################################################################
# Ideas: Recursion 
#        1. If I have n boxes, how can I build a stack with highest height
#        2. Iterate each box as bottom, and for each bottom, I have several possible candidates,
#           how can I build a stack on this bottom with highest height
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
##############################################################################################################################

class Box(object):
	"""A Box with widths, heights and depths"""
	def __init__(self, width, height, depth):
		self.width = width
		self.height = height
		self.depth = depth

	def __str__(self):
		return "({}, {}, {})".format(self.width, self.height, self.depth)
		
class Stack(object):
	"""Stack is a set of boxes"""
	def __init__(self, boxes):
		self.boxes = boxes
		self.cache = {}
		self.talleststack = None

	def tallestStack(self):
		self.talleststack = self.tallestStackRecur(boxes = self.boxes)
		print "Tallest Stack generated successfully!"

	def tallestStackRecur(self, boxes, bottom = None):
		if bottom == None:
			possibleBoxes = boxes
		else:
			if bottom in self.cache:
				return self.cache[bottom]
			# generate possible boxes by comparing the width, height and depth with bottom
			possibleBoxes = []
			for box in boxes:
				if box is bottom or box.width > bottom.width or box.height > bottom.height or box.depth > bottom.depth:
					pass
				else:
					possibleBoxes.append(box)
		maxHeight = 0
		maxHeightStack = []
		for candidate in possibleBoxes:
			substack = self.tallestStackRecur(possibleBoxes, candidate)
			height = reduce(lambda x, y : x + y.height, substack, 0)
			if height > maxHeight:
				maxHeight = height
				maxHeightStack = substack
		
		if bottom == None:
			return maxHeightStack
		else:
			self.cache[bottom] = maxHeightStack + [bottom]
			return self.cache[bottom]

	def printTallestStack(self):
		if self.talleststack is None:
			print "Sorry, you have to generate the tallest stack first!"
		else:
			for box in self.talleststack:
				print box

##############################################################################################################################

def main():
	boxes = [Box(3, 4, 3), Box(2, 3, 1), Box(4, 6, 5), Box(19, 20, 20), Box(10, 16, 18), Box(21, 25, 25), Box(8, 10, 12)]
	mystack = Stack(boxes)
	mystack.printTallestStack()
	mystack.tallestStack()
	mystack.printTallestStack()


if __name__ == '__main__':
	main()
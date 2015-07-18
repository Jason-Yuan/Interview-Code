# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from Stack import *

##############################################################################################################################
# Ideas: Create a minStack to hold the minimum number
# Time Complexity: O(1) for push()/pop()
# Space Complexity: O(n)
##############################################################################################################################

class NewStack():
	def __init__(self):
		self.Stack = Stack()
		self.minStack = Stack()
		self.tempMin = None

	def isEmpty(self):
		return self.Stack.isEmpty()

	def push(self, item):
		if self.tempMin == None or item < self.tempMin:
			self.tempMin = item
		self.Stack.push(item)
		self.minStack.push(self.tempMin)

	def pop(self):
		self.minStack.pop()
		return self.Stack.pop()

	def min(self):
		return self.minStack.peek()

	def peek(self):
		return self.Stack.peek()

	def size(self):
		return self.Stack.size()

##############################################################################################################################

def main():
	# initialize a stack
	mystack = NewStack()

	# push something into a stack
	mystack.push(31)
	mystack.push(52)
	mystack.push(12)
	mystack.push(67)
	mystack.push(49)
	mystack.push(3)
	mystack.push(46)
	mystack.push(31)

	print "Size of the stack: ", mystack.size()
	print "Top of the stack is: ", mystack.peek()
	print "Pop out an item from stack: ", mystack.pop()
	print "Mim of the stack: ", mystack.min()
	mystack.pop()
	mystack.pop()
	mystack.pop()

	print "Mim of the stack: ", mystack.min()

if __name__ == '__main__':
	main()
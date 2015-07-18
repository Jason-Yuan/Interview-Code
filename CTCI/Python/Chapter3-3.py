##############################################################################################################################
# Ideas: 1. Use a list of list to implement the set of stacks
#        2. Add a fixed lenght sub-list into a list if the last list is full
# Time Complexity: O(1) for push() / pop() / popAt()
# Space Complexity: O(n)
##############################################################################################################################

class SetOfStack:
	def __init__(self, threshold):
		self.threshold = threshold
		self.setofstack = []

	def push(self, item):
		# if the outer list is empty or the last list is full, add a new list
		if self.setofstack == [] or len(self.setofstack[-1]) == self.threshold:
			self.setofstack.append([])
		self.setofstack[-1].append(item)

	def pop(self): 
		if self.setofstack == []:
			print "The Stack is empty!"
			return None			
		res = self.setofstack[-1].pop()
		# if the last list is empty, pop out the empty list from the outer list
		if len(self.setofstack[-1]) == 0:
			self.setofstack.pop()
		return res

	def popAt(self, sub_stack):
		if sub_stack + 1 > len(self.setofstack) or sub_stack < 0:
			print "Sub stack index error"
			return None
		return self.setofstack[sub_stack].pop()

##############################################################################################################################

def main():
	# initialize a set of stack
	mystack = SetOfStack(3)

	# push something into a stack
	mystack.push(31)
	mystack.push(52)
	mystack.push(12)
	mystack.push(67)
	mystack.push(49)
	mystack.push(3)
	mystack.push(46)
	mystack.push(31)

	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from sub stack: ", mystack.popAt(0)
	print "Pop out a item from sub stack: ", mystack.popAt(1)
	print "Pop out a item from sub stack: ", mystack.popAt(2)
	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from stack: ", mystack.pop()
	print "Pop out a item from stack: ", mystack.pop()

if __name__ == '__main__':
	main()
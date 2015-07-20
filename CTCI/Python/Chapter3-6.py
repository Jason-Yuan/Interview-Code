# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from Stack import *

##############################################################################################################################
# Ideas: Similar like insertion sort
#        1. Use a temp variable to hold a current max value
#        2. if help stack is empty or help stack.peek() is smaller or equal to max value, push max value to help stack
#        3. if help stack.peek() is largeer than max value, pop the item from help stack to origin stack
#        4. until all sorted, return help stack 
# Time Complexity: O(1) for enquene / O(n) for dequeue 
# Space Complexity: O(n)
##############################################################################################################################

def SortStack(mystack):
	HelpStack = Stack()
	while not mystack.isEmpty():
		MaxValue = mystack.pop()
		while not HelpStack.isEmpty() and HelpStack.peek() > MaxValue:
			mystack.push(HelpStack.pop())
		HelpStack.push(MaxValue)

	return HelpStack

##############################################################################################################################

def main():
	# initialize a stack
	mystack = Stack()
	mystack.push(3)
	mystack.push(1)
	mystack.push(5)
	mystack.push(2)
	mystack.push(4)

	sorted_stack = SortStack(mystack)

	while not sorted_stack.isEmpty():
		print sorted_stack.pop()

if __name__ == '__main__':
	main()
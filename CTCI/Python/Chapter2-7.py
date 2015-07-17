# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *
from Stack import *

##############################################################################################################################
# Ideas: 1. create two pointers, slow runner(one step) and fast runner(two steps) to find the middle of the linked list
#        2. Push the first half into a stack
#        3. Pop out node in the stack and compare with the second half of the linked list
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def IsPalindrome(LL):
	# create a stack to hold the first half of the linked list
	mystack = Stack()

	slow_runner, fast_runner = LL.head, LL.head
	while fast_runner and fast_runner.getNext():
		mystack.push(slow_runner.getData())
		slow_runner = slow_runner.getNext()
		fast_runner = fast_runner.getNext().getNext()

	if fast_runner:
		second_half = slow_runner.getNext()
	else:
		second_half = slow_runner

	result = True
	while second_half != None:
		if mystack.pop() != second_half.getData():
			result = False
		second_half = second_half.getNext()

	return result

##############################################################################################################################

def main():
	# Create a linked list
	myLL = UnorderedLinkedList()
	myLL.add(1)
	myLL.add(2)
	myLL.add(3)
	myLL.add(2)
	myLL.add(1)

	# call the method to check if it's a palindrome
	print "The linked list is: " 
	myLL.Show()
	print "Is the linked list a palindrome? ", IsPalindrome(myLL)

if __name__ == '__main__':
	main()
# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: 1. Cycle detection - Floyd's cycle-finding algorithm
#        2. create two pointers, slow runner(one step) and fast runner(two steps)
#        3. When they first met, put one of them back to head, then move same speed(one step)
#        4. Second time they meet each other, will be at the start point of the loop
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def FindLoopStart(LL):
	slow_runner = LL.head
	fast_runner = LL.head
	while fast_runner and fast_runner.getNext():
		slow_runner = slow_runner.getNext()
		fast_runner = fast_runner.getNext().getNext()
		if slow_runner == fast_runner:
			break

	# return None is its not a cycle linked list
	if not fast_runner or not fast_runner.getNext():
		return None

	slow_runner = LL.head
	while slow_runner != fast_runner:
		slow_runner = slow_runner.getNext()
		fast_runner = fast_runner.getNext()

	return slow_runner.getData()

##############################################################################################################################

def main():
	# Create a cycle linked list
	# Which is 1 2 3 4 5 3 4 5 3 4 5 ......
	cycleLL = UnorderedLinkedList()
	cycleLL.add(5)
	cycleLL.add(4)
	cycleLL.add(3)
	cycleLL.add(2)
	cycleLL.add(1)
	current = cycleLL.head
	while current.getNext() != None:
		current = current.getNext()
	current.setNext(cycleLL.head.getNext().getNext())

	# call the method to find the start point of the loop
	start = FindLoopStart(cycleLL)
	print "The start point of the cycle linked list is: ", start

if __name__ == '__main__':
	main()
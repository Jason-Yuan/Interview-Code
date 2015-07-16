# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: 1. runner technique
#        2. Use two pointers, p1 and p2, let p1 move k steps first, then p1 p2 move together. When p1 move to the end of 
#        the list p2 should be kth to the last node.
#        3. Need to ask if k is longer than the length of the linked list
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def FindKthToLast(LL, k):
	current = LL.head
	runner = LL.head
	# let the runner move k steps first
	counter = 0
	while counter <= k:
		runner = runner.getNext()
		counter += 1

	# then current and runner move together, untill runner arrived at the end
	while runner != None:
		runner = runner.getNext()
		current = current.getNext()

	return current

##############################################################################################################################

def main():
	# Create a linked list
	myLL = UnorderedLinkedList()
	myLL.add(1)
	myLL.add(2)
	myLL.add(3)
	myLL.add(4)
	myLL.add(5)
	myLL.add(6)
	myLL.add(7)
	myLL.add(8)
	print "The original linked list is: "
	myLL.Show()

	# call to get the node kth to the last
	kth_node = FindKthToLast(myLL, 4)
	print "The 4th node to the last is: ", kth_node.getData()

if __name__ == '__main__':
	main()
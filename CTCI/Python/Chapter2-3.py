# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: basic linked list node deletion
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def DeleteMiddleNode(MiddleNode):
	if MiddleNode is None or MiddleNode.getNext() is None:
		return False
	middle = MiddleNode
	next = middle.getNext()
	middle.setData(next.getData())
	middle.setNext(next.getNext())

	return True

##############################################################################################################################

def main():
	# Create a linked list
	myLL = UnorderedLinkedList()
	myLL.add(1)
	myLL.add(2)
	myLL.add(3)
	myLL.add(4)
	myLL.add(5)
	# get the middle node
	MiddleNode = myLL.head.getNext().getNext()

	# call the deletion 
	print "The origin linked list is: "
	myLL.Show()

	if DeleteMiddleNode(MiddleNode):
		print "After deletion:"
		myLL.Show()

if __name__ == '__main__':
	main()
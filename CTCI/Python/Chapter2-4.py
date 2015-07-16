# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: create two dummy node to keep two linked list, one is all node value less that x, another is all node 
#        value greater than or equal to x
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def PartitionByX(LL, x):
	current = LL.head
	# create two dummy node to keep a LL with all node value less than x, 
	# another greater that or equal to x
	dummy1 = UnorderedLinkedList()
	dummy2 = UnorderedLinkedList()
	while current != None:
		if current.getData() < x:
			dummy1.add(current.getData())
		else:
			dummy2.add(current.getData())
		current = current.getNext()

	# Concatinate the two dummy linked list, and return the result
	last = dummy1.head
	while last.getNext() != None:
		last = last.getNext()
	last.setNext(dummy2.head)
	return dummy1

##############################################################################################################################

def main():
	# Create a linked list
	myLL = UnorderedLinkedList()
	myLL.add(12)
	myLL.add(5)
	myLL.add(12)
	myLL.add(7)
	myLL.add(9)
	myLL.add(1)
	myLL.add(2)
	myLL.add(3)
	myLL.add(4)
	myLL.add(5)
	print "The origin linked list is: "
	myLL.Show()

	new_LL = PartitionByX(myLL, 9)
	print "Partition my linked list by 9: "
	new_LL.Show()

if __name__ == '__main__':
	main()
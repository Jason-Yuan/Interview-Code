# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: 1. create a temp variable to hold the carry, iterate the two linked list and add them together
#        2. store the result into the long number, so the space complexity is O(1)
#        3. should be careful about the last node of the long number
#        4. for a FOLLOW UP, just need to reverse the linked list and then call the same method
# Time Complexity: O(n)
# Space Complexity: O(1)
##############################################################################################################################

def LinkedListAdd(LL1, LL2):
	size1 = LL1.size()
	size2 = LL2.size()
	if size1 < size2:
		longNum_current = LL2.head
		shortNum_current = LL1.head
	else:
		longNum_current = LL1.head
		shortNum_current = LL2.head

	carry = 0
	while shortNum_current != None:
		Sum = shortNum_current.getData() + longNum_current.getData() + carry
		if Sum > 9:
			carry = 1
		longNum_current.setData(Sum % 10)

		shortNum_current = shortNum_current.getNext()
		longNum_current = longNum_current.getNext()

	if longNum_current == None:
		last = Node(carry)
		longNum_current.setNext(last)
	else:
		while longNum_current.getNext() != None:
			Sum = longNum_current.getData() + carry
			if Sum > 9:
				carry == 1
			longNum_current.setData(Sum % 10)
			longNum_current = longNum_current.getNext()
		Sum = longNum_current.getData() + carry
		if Sum <= 9:
			longNum_current.setData(Sum)
		else:
			longNum_current.setData(Sum % 10)
			last = Node(1)
			longNum_current.setNext(last)


##############################################################################################################################

def main():
	# Create 2 linked lists as 2 numbers
	myLL_1 = UnorderedLinkedList()
	myLL_1.add(9)
	myLL_1.add(9)
	myLL_1.add(9)
	myLL_1.add(9)
	myLL_1.add(9)
	myLL_1.add(3)
	myLL_1.add(5)
	myLL_1.add(3)

	myLL_2 = UnorderedLinkedList()
	myLL_2.add(8)
	myLL_2.add(2)
	myLL_2.add(4)
	myLL_2.add(2)

	# Show the two numbers will be added:
	print "The numbers will be added:"
	myLL_1.Show()
	myLL_2.Show()

	# call the add method
	LinkedListAdd(myLL_1, myLL_2)
	print "The result is:"
	myLL_1.Show()

if __name__ == '__main__':
	main()
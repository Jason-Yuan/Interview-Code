# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Method 1 
# Ideas: Without extra buffer, we need to use nested loop to solve this.
# Time Complexity: O(n2)
# Space Complexity: O(1)
##############################################################################################################################

def DeleteDuplicates1(LL):
	current = LL.head
	while current != None:
		# iterate each node after current, delete the duplicate ones
		pre_check = current
		check = current.getNext()
		while check != None:
			if check.getData() == current.getData():
				pre_check.setNext(check.getNext())
				check = check.getNext()
			else:
				pre_check = check
				check = check.getNext()

		current = current.getNext()

##############################################################################################################################
# Method 2
# Ideas: With extra buffer, we use a hash table to store each node and we only need to loop once to delete the diplicates.
# Info: 1. Python's built-in hash table implementation, in the form of the dict type.
#       2. Python sets also use hashes internally, for fast lookup (though they store only keys, not values).
#       3. In some rare cases the contains, get item, and set item operations can degenerate into O(n) performance.
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def DeleteDuplicates2(LL):
	HashTable = set()
	current = LL.head
	previous = None
	while current != None:
		if current.getData() in HashTable:
			previous.setNext(current.getNext())
			current = current.getNext()
		else:
			HashTable.add(current.getData())
			previous = current
			current = current.getNext()
		
##############################################################################################################################

def main():
	# Create 2 linked list
	myLL_1 = UnorderedLinkedList()
	myLL_1.add(1)
	myLL_1.add(1)
	myLL_1.add(2)
	myLL_1.add(3)
	myLL_1.add(3)
	myLL_1.add(3)
	myLL_1.add(4)
	myLL_1.add(5)

	myLL_2 = UnorderedLinkedList()
	myLL_2.add(1)
	myLL_2.add(1)
	myLL_2.add(2)
	myLL_2.add(3)
	myLL_2.add(3)
	myLL_2.add(3)
	myLL_2.add(4)
	myLL_2.add(5)

	print "The original linked list 1 is: "
	myLL_1.Show()
	# Calling the first method to delete the duplicates
	DeleteDuplicates1(myLL_1)
	print "The linked list after first deletion method: "
	myLL_1.Show()

	print "The original linked list 2 is: "
	myLL_2.Show()
	# Calling the first method to delete the duplicates
	DeleteDuplicates2(myLL_2)
	print "The linked list after first deletion method: "
	myLL_2.Show()

if __name__ == '__main__':
	main()
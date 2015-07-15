##############################################################################################################################
#      Project:                  Ordered Linked List 
#      Info:                     1. Node is the basic building block for the linked list implementation.
#    							 2. For each node, it contains a data and a address point to the next node.
#                                3. ONLY the add() method is different from unordered linked list
##############################################################################################################################

# Node Implementation
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Ordered List Implementation
class UnorderedLinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
    	return self.head == None

    def add(self,item):
        current = self.head
        previous = None
        while current != None and current.getData() <= item:
            previous = current
            current = current.getNext()

        temp = Node(item)
        if previous == None: # which means the new item is the smallest
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
    	current = self.head
    	count = 0
    	while current != None:
    		count = count + 1
    		current = current.getNext()

    	return count

    def search(self,item):
    	current = self.head
    	found = False
    	while current != None and not found:
    		if current.getData() == item:
    			found = True
    		else:
    			current = current.getNext()

    	return found

    def remove(self,item):
    	current = self.head
    	previous = None
    	found = False
    	while not found:
    		if current.getData() == item:
    			found = True
    		else:
    			previous = current
    			current = current.getNext()

    	if previous == None:
    		self.head = current.getNext()
    	else:
    		previous.setNext(current.getNext())

    def Show(self):
    	current = self.head
    	while current != None:
    		print current.data
    		current = current.getNext()

##############################################################################################################################

def main():
	myLL = UnorderedLinkedList()
	myLL.add(10)
	myLL.add(3)
	myLL.add(4)
	myLL.add(6)
	myLL.add(1)
	myLL.add(9)
	print "Size of myLL is: ", myLL.size()
	myLL.Show()

	print "Remove 10 from the unordered linked list..."
	myLL.remove(10)
	myLL.Show()

	print "Check if myLL contains 1: ", myLL.search(1)

if __name__ == '__main__':
	main()
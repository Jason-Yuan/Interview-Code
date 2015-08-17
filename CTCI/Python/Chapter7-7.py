##############################################################################################################################
# Ideas: 1. Maintain three queue as Q3 Q5 and Q7
#        2. each time find the smallest one and append 3*small 5 *small and 7*small to the queue accordingly 
#           except teh duplicates
##############################################################################################################################

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

def kthNumber(k):
	if k < 1:
		return "Error"
	q3 = Queue()
	q5 = Queue()
	q7 = Queue()

	q3.enqueue(3)
	q5.enqueue(5)
	q7.enqueue(7)

	count = 0
	while count < k:
		count += 1
		ret = min(q3.peek(), min(q5.peek(), q7.peek()))
		if ret == q3.peek():
			q3.dequeue()
			q3.enqueue(3 * ret)
			q5.enqueue(5 * ret)
			q7.enqueue(7 * ret)
		elif ret == q5.peek():
			q5.dequeue()
			q5.enqueue(5 * ret)
			q7.enqueue(7 * ret)
		else:
			q7.dequeue()
			q7.enqueue(7 * ret)

	return ret

##############################################################################################################################

def main():
	for i in range(1, 10):
		print "The {}'s number is {}".format(i, kthNumber(i))

if __name__ == '__main__':
	main()
##############################################################################################################################
# Ideas: Evenly seperate the array into three sections
# Time Complexity: O(1) for push()/pop()
# Space Complexity: O(n)
##############################################################################################################################

class ArrayStack():
	"""Implement three stacks use a single array"""
	def __init__(self):
		self.array = [0 for i in range(30)]
		self.top = [-1, 9, 19]

	def pop(self, stack_num):
		if self.top[stack_num] == stack_num * 10 - 1:
			print "Empty stack"
			return False
		ret = self.array[self.top[stack_num]]
		self.array[self.top[stack_num]] = 0
		self.top[stack_num] -= 1

	def push(self, stack_num, item):
		if self.top[stack_num] == (stack_num + 1) * 10 - 1:
			print "Stack Overflow"
			return

		self.top[stack_num] += 1
		self.array[self.top[stack_num]] = item

	def isEmpty(self, stack_num):
		if self.top[stack_num] == stack_num * 10 - 1:
			return True
		else:
			return False

	def peek(self, stack_num):
		if self.top[stack_num] == stack_num * 10 - 1:
			print "Empty stack"
			return False
		return self.array[self.top[stack_num]]
		
##############################################################################################################################

def main():
    # initialize a stack
    mystack = ArrayStack()

    # push something into the stack
    mystack.push(0, 10)
    mystack.push(1, 10)
    mystack.push(2, 10)
    mystack.push(2, 3)
    mystack.push(2, 1)
    mystack.push(2, 4)

    print "Top of the stack 1 is: ", mystack.peek(0)
    print "Top of the stack 2 is: ", mystack.peek(1)
    print "Top of the stack 3 is: ", mystack.peek(2)
    
if __name__ == '__main__':
	main()
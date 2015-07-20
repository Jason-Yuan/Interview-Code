import datetime

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

##############################################################################################################################
# Ideas: Define two queue in the AnimalQueue class also define a cat class and a dog class
#        use datatime.datetime.now() to keep record 
# Time Complexity: O(1) for enqueueAny
#                  O(1) for dequeueDog
#                  O(1) for dequeueCat 
#                  O(1) for enqueue
# Space Complexity: O(n)
##############################################################################################################################

class Animal(object):
	def __init__(self, Name):
		self.name = Name
		self.time = datetime.datetime.now()

class Cat(Animal):
	def __init__(self, Name):
		Animal.__init__(self, Name)
		self.category = "cat"

class Dog(Animal):
	def __init__(self, Name):
		Animal.__init__(self, Name)
		self.category = "dog"

class AnimalQueue(object):
	def __init__(self):
		self.DogQueue = Queue()
		self.CatQueue = Queue()

	def enqueue(self, animal):
		if animal.category == "dog":
			self.DogQueue.enqueue(animal)
		elif animal.category == "cat":
			self.CatQueue.enqueue(animal)
		else:
			print "We only accept cats and dogs."
			return

	def dequeueAny(self):
		if self.CatQueue.isEmpty() and self.DogQueue.isEmpty():
			return
		elif self.CatQueue.isEmpty():
			return self.DogQueue.dequeue()
		elif self.DogQueue.isEmpty():
			return self.CatQueue.dequeue()
		else:
			if self.CatQueue.peek().time > self.DogQueue.peek().time:
				return self.DogQueue.dequeue()
			else:
				return self.CatQueue.dequeue()

	def dequeueDog(self):
		if self.DogQueue.isEmpty():
			return
		return self.DogQueue.dequeue()

	def dequeueCat(self):
		if self.CatQueue.isEmpty():
			return 
		return self.CatQueue.dequeue()

##############################################################################################################################

def main():
	# define some animals
	cat1 = Cat("Lucy")
	cat2 = Cat("Marry")
	dog1 = Dog("Tom")
	dog2 = Dog("Andrew")
	# define a shelter
	shelter = AnimalQueue()

	shelter.enqueue(cat1)
	shelter.enqueue(dog2)
	shelter.enqueue(dog1)
	shelter.enqueue(cat2)

	print "Get the first dog which is: ", shelter.dequeueDog().name
	print "Get the first cat which is: ", shelter.dequeueCat().name
	print "Get the first animal which is: ", shelter.dequeueAny().name

if __name__ == '__main__':
	main()
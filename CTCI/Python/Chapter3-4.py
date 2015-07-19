# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from Stack import *

##############################################################################################################################
# Ideas: classic problem of the Towers of Hanoi - Recursion 
# Time Complexity: O(2**n) 
# Space Complexity: O(n)
##############################################################################################################################

class Tower():
    def __init__(self, Name):
    	self.stack = Stack()
    	self.name = Name

    def moveDisk(self, toTower):
        disk = self.stack.pop()
        toTower.stack.push(disk)
        print "Move Disk", disk, "from tower", self.name, "to tower", toTower.name 

    def moveTower(self, height, destination, buffer):
        if height <= 0: return
        self.moveTower(height - 1, buffer, destination)
        self.moveDisk(destination)
        buffer.moveTower(height - 1, destination, self)

    def add(self, disk):
    	if self.stack.size() != 0 and self.stack.peek() < disk:
    		print "Please add an disk smaller than the current top"
    		return
        self.stack.push(disk)

##############################################################################################################################

def main():
	n = 3
	towerA = Tower("A")
	towerB = Tower("B")
	towerC = Tower("C")
	for i in reversed(range(n)): towerA.add(i+1)
	towerA.moveTower(n, towerB, towerC)

if __name__ == '__main__':
	main()
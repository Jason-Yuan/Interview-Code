# import the dependent packages
import sys
sys.path.append('../../Basic Data Structure')
from LinkedList import *

##############################################################################################################################
# Ideas: BFS, 
# Time Complexity: O(n)
# Space Complexity: O(h) (h is height of tree)
##############################################################################################################################

class DirectedGraphNode:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

def treeToLinkedList(root):
	result = []
	if not root:
		return 
	else:
		temp = UnorderedLinkedList()
		temp.add(root.key)
		result.append(temp)

		level = {root:0}
		i = 1
		frontier = [root]
		while frontier:
			next = []
			temp = UnorderedLinkedList()
			for node in frontier:
				for neighbor in node.neighbors:
					if neighbor not in level:
						level[neighbor] = i
						next.append(neighbor)
						i += 1
			for item in next:
				temp.add(item.key)
			if not temp.isEmpty():
				result.append(temp)
			frontier = next
		return result

##############################################################################################################################

def main():
    A = DirectedGraphNode('A')
    B = DirectedGraphNode('B')
    C = DirectedGraphNode('C')
    D = DirectedGraphNode('D')
    E = DirectedGraphNode('E')

    A.neighbors.append(B)
    A.neighbors.append(D)
    B.neighbors.append(C)
    B.neighbors.append(D)
    D.neighbors.append(E)

    print treeToLinkedList(A)

    for i in treeToLinkedList(A):
    	i.Show()

if __name__ == '__main__':
		main()	
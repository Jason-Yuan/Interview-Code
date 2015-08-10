##############################################################################################################################
# Ideas: BFS
# Time Complexity: O(V+E)
# Space Complexity: O(V) 
# info:
# A----->B----->C
#  \     |
#   \    |
#    \   |
#     \  v
#      ->D----->E
##############################################################################################################################

class DirectedGraphNode:
    def __init__(self, key):
        self.key = key
        self.neighbors = []

def hasRoute(s, t):
    if s == t:
        return True
    elif s == None or t == None:
        return False
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for node in frontier:
            for neighbor in node.neighbors:
                if neighbor not in level:
                    if neighbor == t:
                        return True
                    level[neighbor] = i
                    parent[neighbor] = node
                    next.append(neighbor)
        frontier = next
    return False

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

    print "Is there a path from A to E? ", hasRoute(A, E)
    print "Is there a path from A to A? ", hasRoute(A, A)
    print "Is there a path from D to B? ", hasRoute(D, B)

if __name__ == '__main__':
	main()
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
            
        nodes = []
        # BFS clone node
        nodes.append(node)
        self.dict[node] = UndirectedGraphNode(node.label)
        pointer = 0
        while pointer < len(nodes):
            for neighbor in nodes[pointer].neighbors:
                if neighbor not in self.dict:
                    nodes.append(neighbor)
                    self.dict[neighbor] = UndirectedGraphNode(neighbor.label)
            pointer += 1
                    
        # clone neighbors
        for n in nodes:
            newNode = self.dict[n]
            for neighbor in n.neighbors:
                newNode.neighbors.append(self.dict[neighbor])
                
        return self.dict[node]
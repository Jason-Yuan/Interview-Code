# Method 1: BFS
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import Queue

class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
            
        newHead = UndirectedGraphNode(node.label)
        self.visited[node] = newHead
        
        myQueue = Queue.Queue()
        myQueue.put(node)
        while myQueue.qsize():
            current = myQueue.get()
            for neighbor in current.neighbors:
                if neighbor not in self.visited:
                    newNode = UndirectedGraphNode(neighbor.label)
                    self.visited[current].neighbors.append(newNode)
                    self.visited[neighbor] = newNode
                    myQueue.put(neighbor)
                else: # turn directed graph to undirected graph
                    self.visited[current].neighbors.append(self.visited[neighbor])
                    
        return newHead

# Method 2: DFS
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
            
        return self.dfs(node, {})
        
    def dfs(self, node, map):
        if node in map:
            return map[node]
        newNode = UndirectedGraphNode(node.label)
        map[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.dfs(neighbor, map))
            
        return newNode
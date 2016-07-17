# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        self.hashMap = {}
        for node in nodes:
            self.hashMap[node.label] = False
            
        res = []
        for node in nodes:
            if not self.hashMap[node.label]:
                temp = []
                self.dfs(node, temp)
                res.append(sorted(temp))
                
        return res
        
    def dfs(self, node, temp):
        self.hashMap[node.label] = True
        temp.append(node.label)
        for neighbor in node.neighbors:
            if not self.hashMap[neighbor.label]:
                self.dfs(neighbor, temp)
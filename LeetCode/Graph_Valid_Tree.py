class UnionFind:
    def __init__(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i 
  
    def compressed_find(self, x):
        parent = self.father[x]
        while parent != self.father[parent]:
            parent = self.father[parent]

        temp = -1;
        fa = self.father[x]
        while fa != self.father[fa]:
            temp = self.father[fa]
            self.father[fa] = parent
            fa = temp

        return parent

        
    def union(self, x, y):
            fa_x = self.compressed_find(x)
            fa_y = self.compressed_find(y)
            if fa_x != fa_y:
                self.father[fa_x] = fa_y

class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        if len(edges) != n - 1:
            return False
            
        uf = UnionFind(n)
        
        for edge in edges:
            pointA, pointB = edge[0], edge[1]
            fpointA = uf.compressed_find(pointA)
            fpointB = uf.compressed_find(pointB)
            if fpointA == fpointB:
                return False
            else:
                uf.union(pointA, pointB)
                
        return True
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class UnionFind:
    def __init__(self, m, n):
        self.father = {}
        for i in range(n):
            for j in range(m):
                id = self.converttoId(i,j,m);
                self.father[id] = id 

    def converttoId(self, x, y, m):
        return x*m + y
        
    def find(self, x):
            parent = self.father[x]
            while parent != self.father[parent]:
                parent = self.father[parent]
            return parent
        
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
            fa_x = self.find(x)
            fa_y = self.find(y)
            if fa_x != fa_y:
                self.father[fa_x] = fa_y
                
class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        dx = [0,-1, 0, 1]
        dy = [1, 0, -1, 0]
        island = [[0 for i in range(m)] for j in range(n)]
        ans = []
        uf = UnionFind(n, m)
        count = 0
        if operators != None:
            for i in range(len(operators)):
                count += 1
                x = operators[i].x
                y = operators[i].y
                if island[x][y] != 1:
                    island[x][y]  = 1
                    id = uf.converttoId(x, y, m)
                    # 计算上下左右四个点的位置
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx and nx < n and 0 <= ny and ny < m and island[nx][ny] == 1:
                            nid = uf.converttoId(nx, ny, m)
                            fa = uf.find(id)
                            nfa = uf.find(nid)
                            if fa != nfa:
                                count -= 1
                                uf.union(id, nid)

                ans.append(count)
            return ans
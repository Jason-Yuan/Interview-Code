class Solution(object):
    def __init__(self):
        self.dx = [1, 0, 0, -1]
        self.dy = [0, 1, -1, 0]
        self.m = 0
        self.n = 0
    
    def removeIsland(self, grid, x, y):
        grid[x][y] = '0';
        for i in range(4):
            nextX = x + self.dx[i]
            nextY = y + self.dy[i]
            if nextX >= 0 and nextX < self.n and nextY >= 0 and nextY < self.m:
                if grid[nextX][nextY] == '1':
                    self.removeIsland(grid, nextX, nextY)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.n = len(grid)
        if self.n == 0:
            return 0
        
        self.m = len(grid[0])
        if self.m == 0:
            return 0
        
        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    self.removeIsland(grid, i, j)
                    count += 1
        
        return count
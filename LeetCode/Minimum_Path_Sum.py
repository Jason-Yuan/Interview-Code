class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        cache = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        cache[0][0] = grid[0][0]
        
        for i in range(1, len(grid)):
            cache[i][0] = cache[i - 1][0] + grid[i][0]
        
        for i in range(1, len(grid[0])):
            cache[0][i] = cache[0][i - 1] + grid[0][i]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                cache[i][j] = min(cache[i][j - 1], cache[i - 1][j]) + grid[i][j]
            
        return cache[len(grid) - 1][len(grid[0]) - 1]
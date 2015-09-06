class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 
        r, c = len(grid), len(grid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = grid[0][0]
        for i in xrange(1, r):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in xrange(1, c):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in xrange(1, len(grid)):
            for j in xrange(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        temp1 = temp2 = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                temp1 = 0
            dp[0][j] = temp1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                temp2 = 0
            dp[i][0] = temp2
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        n = len(triangle)
        sum = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            sum[n - 1][i] = triangle[n - 1][i]

        for i in range(n - 2, -1, -1): 
            for j in range(i + 1):
                sum[i][j] = min(sum[i + 1][j], sum[i + 1][j + 1]) + triangle[i][j]

        return sum[0][0]
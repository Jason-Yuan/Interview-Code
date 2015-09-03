class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return -1
        T = [None] * (n+1)
        for i in range(n+1):
            if i < 1:
                T[i] = 1
            elif i == 1:
                T[i] = 1
            else:
                T[i] = T[i - 1] + T[i - 2]
        return T[n]
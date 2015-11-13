class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0 for i in range(n)]
        res[0] = 1
        i2 = i3 = i5 = 0
        for i in range(1, n):
            nextUglyNumber = min(min(res[i2] * 2, res[i3] * 3), res[i5] * 5)
            if nextUglyNumber == res[i2] * 2:
                i2 += 1
            if nextUglyNumber == res[i3] * 3:
                i3 += 1
            if nextUglyNumber == res[i5] * 5:
                i5 += 1
            res[i] = nextUglyNumber
        return res[n - 1]
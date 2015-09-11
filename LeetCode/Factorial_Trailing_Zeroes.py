class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
            
        i, count = 5, 0
        while n / i > 0:
            count += n / i
            i *= 5
            
        return count
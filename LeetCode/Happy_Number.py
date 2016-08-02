class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        myset = set()
        while n != 1 and n not in myset:
            myset.add(n)
            n = self.helper(n)
        return n == 1
        
    def helper(self, num):
        res = 0
        while num:
            res += (num % 10) * (num % 10)
            num /= 10
        return res
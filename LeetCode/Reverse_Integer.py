class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            res = self.helper(x)
        else:
            res =  -self.helper(-x)
        return res if -2147483648 <= res <= 2147483647 else 0
        
    def helper(self, num):
        res = 0
        while num > 0:
            res *= 10
            res += num % 10
            num /= 10
        return res
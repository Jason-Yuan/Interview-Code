class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
            
        temp = x
        revt = 0
        while temp:
            revt = revt * 10 + temp % 10
            temp /= 10
        return revt == x
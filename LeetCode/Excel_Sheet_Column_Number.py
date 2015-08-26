class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 
        res = 0
        base = 1
        for i in range(len(s) - 1, -1, -1):
            res += base * (ord(s[i]) - 64)
            base *= 26
        return res
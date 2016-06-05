class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):   #avoid TLE(Time Limited Exceeded)
            return False
        cache = [[False for i in range(len(s) + 1)] for j in range(2)]
        cache[0][0] = True
        for j in range(1, len(p) + 1):
            cache[j % 2][0] = cache[(j - 1) % 2][0] and p[j - 1] == "*"
            for i in range(1, len(s) + 1):
                cache[j % 2][i] = False
                if s[i - 1] == p[j - 1] or s[i - 1] == "?" or p[j - 1] == "?":
                    cache[j % 2][i] = cache[(j - 1) % 2][i - 1]
                if s[i - 1] == "*" or p[j - 1] == "*":
                    cache[j % 2][i] = cache[(j - 1) % 2][i] or cache[j % 2][i - 1]
        return cache[len(p) % 2][len(s)]
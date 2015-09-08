class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s:
            return 0
        if not t:
            return 1
            
        cache = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        
        for j in range(len(s) + 1):
            cache[j][0] = 1
            
        for j in range(1, len(s) + 1):
            for i in range(1, len(t) + 1):
                if t[i - 1] == s[j - 1]:
                    cache[j][i] = cache[j - 1][i] + cache[j - 1][i - 1]
                else:
                    cache[j][i] = cache[j - 1][i]
                    
        return cache[len(s)][len(t)]
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
            
        cache = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        
        cache[0][0] = True
        for i in range(1, len(s1) + 1):
            if cache[0][i -1] and s1[i - 1] == s3[i - 1]:
                cache[0][i] = True
            else:
                break
                
        for j in range(1, len(s2) + 1):
            if cache[j - 1][0] and s2[j - 1] == s3[j - 1]:
                cache[j][0] = True
            else:
                break
                
        for j in range(1, len(s2) + 1):
            for i in range(1, len(s1) + 1):
                if (cache[j - 1][i] and s2[j - 1] == s3[j + i - 1]) or (cache[j][i - 1] and s1[i - 1] == s3[j + i - 1]):
                    cache[j][i] = True
                
        return cache[len(s2)][len(s1)]
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
            
        cache = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        
        for i in range(1, len(word1) + 1):
            cache[0][i] = i
        for j in range(1, len(word2) + 1):
            cache[j][0] = j
            
        for j in range(1, len(word2) + 1):
            for i in range(1, len(word1) + 1):
                if word1[i - 1] == word2[j - 1]:
                    cache[j][i] = min(cache[j - 1][i - 1], # substitute
                                      cache[j - 1][i] + 1, # insert
                                      cache[j][i - 1] + 1) # delete
                else:
                    cache[j][i] = min(cache[j - 1][i - 1], cache[j - 1][i], cache[j][i - 1]) + 1
        
        return cache[len(word2)][len(word1)]
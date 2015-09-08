class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False
        
        maxLength = self.getMaxLength(wordDict)
        cache = [False] * (len(s) + 1)
        cache[0] = True
        
        for i in range(1, len(s) + 1):
            j = 1
            while j <= maxLength and j <= i:
                if not cache[i - j]:
                    j += 1
                    continue
                if s[i - j:i] in wordDict:
                    cache[i] = True
                    break
                j += 1
                
        return cache[len(s)]
                

    def getMaxLength(self, dict):
        maxLength = 0
        for word in dict:
            maxLength = max(len(word), maxLength)
        return maxLength
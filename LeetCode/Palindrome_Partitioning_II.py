class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        IsPalindrome = self.getIsPalindrome(s)
        cache = [0 for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            cache[i] = i - 1
            
        for i in range(1, len(s) + 1):
            for j in range(i):
                if IsPalindrome[j][i - 1]:
                    cache[i] = min(cache[i], cache[j] + 1)
                    
        return cache[len(s)]
        
    
    def getIsPalindrome(self, str):
        IsPalindrome = [[False for i in range(len(str))] for i in range(len(str))]
        """
        initialize (0, 0), (1, 1)......
        and (0, 1), (1, 2)......
        """
        for i in range(len(str)):
            IsPalindrome[i][i] = True
        for i in range(len(str) - 1):
            if str[i] == str[i + 1]:
                IsPalindrome[i][i + 1] = True
                
        for length in range(2, len(str)):
            for start in range(0, len(str) - length):
                IsPalindrome[start][start + length] = \
                IsPalindrome[start + 1][start + length - 1] and str[start] == str[start + length]
                
        return IsPalindrome
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
            
        cache = [0 for i in range(len(s) + 1)]
        cache[0] = cache[1] = 1
        for i in range(2, len(s) + 1):
            num = int(s[i-2:i])
            if num == 0 or (s[i - 1] == "0" and num > 26): # 100 or 130
                cache[i] = 0
            elif num < 10: # 109
                cache[i] = cache[i - 1]
            elif num < 27: 
                if num == 10 or num == 20: # 110 or 120
                    cache[i] = cache[i - 2]
                else: # 117, 126 ...
                    cache[i] = cache[i - 1] + cache[i - 2]
            else: # 127, 178
                cache[i] = cache[i - 1]
                
        return cache[len(s)]
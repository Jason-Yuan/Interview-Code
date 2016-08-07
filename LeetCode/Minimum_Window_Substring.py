class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(t) > len(s):
            return ""
        right, res = 0, []
        length = sys.maxint
        sourceHash, targetHash = {}, {}
        for char in t:
            if char not in targetHash:
                targetHash[char] = 1
            else:
                targetHash[char] += 1
                
        for left in range(len(s)):
            while not self.valid(sourceHash, targetHash) and right < len(s):
                if s[right] not in sourceHash:
                    sourceHash[s[right]] = 1
                else:
                    sourceHash[s[right]] += 1
                right += 1
            if self.valid(sourceHash, targetHash) and right - left< length:
                length = right - left
                res = [left, right]
            sourceHash[s[left]] -= 1
        
        return "" if not res else s[res[0]:res[1]]
        
    def valid(self, sourceHash, targetHash):
        for key, value in targetHash.items():
            if key not in sourceHash:
                return False
            elif key in sourceHash and targetHash[key] > sourceHash[key]:
                return False
        return True
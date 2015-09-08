class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        return reduce(self.getLCP, strs)
        
    def getLCP(self, str1, str2):
        n, lcp = min(len(str1), len(str2)), ""
        
        for i in range(n):
            if str1[i] != str2[i]:
                break
            else:
                lcp += str1[i]
        return lcp
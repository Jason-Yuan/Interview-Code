class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s is None:
            return [[]]
        path = []
        result = []
        self.helper(s, path, result)
        return result  
        
    def helper(self, s, path, result):
        if not s:
            result.append(path)
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.isPalindrome(prefix):
                self.helper(s[i:], path + [prefix], result)

    def isPalindrome(self, string):
        return string == string[::-1]
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, res = 0, 0
        LastAppeared = {}
        for right in range(len(s)):
            if s[right] in LastAppeared and LastAppeared[s[right]] >= left:
                left = LastAppeared[s[right]] + 1
            LastAppeared[s[right]] = right
            res = max(res, right - left + 1)
        return res
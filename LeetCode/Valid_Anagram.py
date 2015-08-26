class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None or len(s) != len(t):
            return False
        map = {}
        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
        
        for char in t:
            if char in map:
                map[char] -= 1
        
        for key, value in map.iteritems():
            if value != 0:
                return False
            
        return True
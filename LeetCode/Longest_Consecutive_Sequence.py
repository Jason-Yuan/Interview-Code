class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        for e in nums:
            if e not in map:
                map[e] = 1
        res = 0        
        for e in nums:
            if map[e] != -1:
                temp = map[e]
                lg = sm = e
                while lg + 1 in map and map[lg + 1] != -1:
                    temp += map[lg + 1]
                    map[lg + 1] = -1
                    lg += 1
                while sm - 1 in map and map[sm - 1] != -1:
                    temp += map[sm - 1]
                    map[sm - 1] = -1
                    sm -= 1
            if temp > res:
                res = temp     
        return res
# Iteratively
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return
        nums.sort()
        ret = [[]]
        for x in nums:
            with_x = []
            for res in ret:
                with_x.append(res + [x])
            ret += with_x
        return ret

# Bit Manipulation
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        nums.sort()
        limit = 1 << len(nums)    # for [1, 2, 3], the limit = 1000(binary), largest current = 111(binary)
        
        current = 0     # current = 000 => []
        result = []
        
        while current < limit:
            subset = []
            for index in xrange(len(nums)):
                if (1 << index) & current != 0:
                    subset.append(nums[index])
            result.append(subset)
            current += 1    # from 000 -> 001 -> 010 -> 011 -> 100 -> 101 -> 110 -> 111
            
        return result

# DFS recursively (56ms)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = [[]]
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        for i in xrange(index, len(nums)):
            res.append(path + [nums[i]])
            self.dfs(nums, i+1, path+[nums[i]], res)
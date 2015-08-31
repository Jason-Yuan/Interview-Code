# Non-Recursion
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if nums == []:
            return [[]]
        res = []
        for i in range(len(nums)):
            temp = self.permute(nums[:i] + nums[i+1:])
            for subarray in temp:
                res.append(subarray + [nums[i]])
        return res


# Backtracking
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        result = []
        self.helper(nums, [], result)
        return result
        
    def helper(self, List, path, result):
        if len(path) == len(List):
            result.append(path[:])
            return
        
        for i in range(len(List)):
            if List[i] in path:
                continue
            path.append(List[i])
            self.helper(List, path, result)
            path.pop()
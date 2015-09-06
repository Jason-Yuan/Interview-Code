# Greedy 
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
           
        start = end = steps = 0 
        while end < len(nums) - 1:
            steps += 1
            farthest = end
            for i in range(start, end + 1):
                if nums[i] + i > farthest:
                    farthest = nums[i] + i
            start = end + 1
            end = farthest
            
        return steps


# DP
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = [-1 for i in range(len(nums))]
        steps[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if steps[j] != -1 and nums[j] + j >= i:
                    steps[i] = steps[j] + 1
                    break
        return steps[len(nums) - 1]
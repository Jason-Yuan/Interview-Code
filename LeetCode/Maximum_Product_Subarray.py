class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCache = [0 for i in range(len(nums))]
        minCache = [0 for i in range(len(nums))]
        
        minCache[0] = maxCache[0] = nums[0];
        result = nums[0]
        for i in range(1, len(nums)):
            minCache[i] = maxCache[i] = nums[i]
            if nums[i] > 0:
                maxCache[i] = max(maxCache[i], maxCache[i - 1] * nums[i])
                minCache[i] = min(minCache[i], minCache[i - 1] * nums[i])
            elif nums[i] < 0:
                maxCache[i] = max(maxCache[i], minCache[i - 1] * nums[i])
                minCache[i] = min(minCache[i], maxCache[i - 1] * nums[i])
            
            result = max(result, maxCache[i])
        
        return result
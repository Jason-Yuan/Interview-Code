class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        res, sum, minSum = -sys.maxint - 1, 0, 0
        for num in nums:
            sum += num
            res = max(res, sum - minSum)
            minSum = min(minSum, sum)

        return res
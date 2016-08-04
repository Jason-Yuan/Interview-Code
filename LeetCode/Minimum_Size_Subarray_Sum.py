class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        right, sum = 0, 0
        res = sys.maxint
        for left in range(len(nums)):
            while right < len(nums) and sum < s:
                sum += nums[right]
                right += 1
            if sum >= s:
                res = min(res, right - left)
            sum -= nums[left]    
        if res == sys.maxint:
            return 0
        return res
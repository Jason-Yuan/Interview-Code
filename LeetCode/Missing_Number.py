class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            0
        sum = len(nums) * (len(nums) + 1) / 2
        temp = 0
        for num in nums:
            temp += num
        return sum - temp
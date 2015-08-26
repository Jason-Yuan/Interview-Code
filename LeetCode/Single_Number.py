class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for item in nums:
            res ^= item
        return res
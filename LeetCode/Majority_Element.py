class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]
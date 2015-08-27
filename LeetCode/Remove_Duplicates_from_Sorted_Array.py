# Method 1
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = None
        length = 0
        for x in nums:
            if x != prev:
                prev = x
                nums[length] = x
                length += 1
        return length

# Method 2
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                nums.remove(nums[i+1])
                length -= 1
            i += 1
        return length
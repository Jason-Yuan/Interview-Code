class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = None
        prev = None
        length = 0
        for x in nums:
            if x != prev:
                nums[length] = x
                length += 1
                prev = x
            elif x != slow:
                nums[length] = x
                length += 1
                slow = prev
                prev = x
        return length
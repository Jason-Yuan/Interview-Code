class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            if start == end:
                return start
            mid = (start + end) / 2
            if nums[mid] < nums[mid + 1]:
                start = mid + 1
            else:
                end = mid
        return mid
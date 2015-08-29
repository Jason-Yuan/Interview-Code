class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            while nums[mid] == nums[start] and start < mid:
                start += 1
            while nums[mid] == nums[end] and end > mid:
                end -= 1
            if nums[mid] > nums[end]:
                start = mid
            elif nums[mid] < nums[end]:
                end = mid
                
        return min(nums[start], nums[end])
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return True
            while nums[mid] == nums[start] and start < mid:
                start += 1
            while nums[mid] == nums[end] and end > mid:
                end -= 1
            if nums[mid] > nums[end]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target or nums[end] == target:
            return True
        return False
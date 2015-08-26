class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        left = right = None
        while start <= end:
            mid = (start + end) / 2
            if nums[mid] == target:
                leftEnd = rightStart = mid
                while start <= leftEnd:
                    left = (start + leftEnd) / 2
                    if nums[left] == target:
                        leftEnd = left - 1
                    else:
                        start = left + 1
                if nums[left] != target:
                    left += 1
                while rightStart <= end:
                    right = (rightStart + end) / 2
                    if nums[right] == target:
                        rightStart = right + 1
                    else:
                        end = right - 1
                if nums[right] != target:
                    right -= 1
                return [left, right]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return [-1, -1]
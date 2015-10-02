class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        i = 0
        redIndex, blueIndex = 0, len(nums) - 1
        while i <= blueIndex:
            if nums[i] == 0:
                nums[i], nums[redIndex] = nums[redIndex], nums[i]
                i += 1
                redIndex += 1
                continue
            elif nums[i] == 2:
                nums[i], nums[blueIndex] = nums[blueIndex], nums[i]
                blueIndex -= 1
                continue
            i += 1
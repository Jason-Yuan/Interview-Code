class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) < 2:
            pass

        # find the last increase index    
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        if index != -1:
            # find the first bigger one
            biggerIndex = index + 1
            for i in range(len(nums) - 1, index, -1):
                if nums[i] > nums[index]:
                    biggerIndex = i
                    break
        
            # swap them to make the permutation bigger
            nums[index], nums[biggerIndex] = nums[biggerIndex], nums[index]
        
        # reverse the last part
        m, n = index + 1, len(nums) - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
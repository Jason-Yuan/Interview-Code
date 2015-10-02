class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return res
            
        sortNum = sorted(nums)
        for i in range(len(sortNum)):
            if i != 0 and sortNum[i] == sortNum[i - 1]:
                continue
            target = - sortNum[i]
            left, right = i + 1, len(sortNum) - 1
            while left < right:
                if sortNum[left] + sortNum[right] == target:
                    res.append([sortNum[i], sortNum[left], sortNum[right]])
                    left += 1
                    right -= 1
                    while left < right and sortNum[left] == sortNum[left - 1]:
                        left += 1
                    while left < right and sortNum[right] == sortNum[right + 1]:
                        right -= 1
                elif sortNum[left] + sortNum[right] > target:
                    right -= 1
                else:
                    left += 1
                    
        return res
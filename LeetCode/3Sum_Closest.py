class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return []
            
        sortNum = sorted(nums)
        closest = sys.maxint
        for i in range(len(sortNum)):
            left, right = i + 1, len(sortNum) - 1
            while left < right:
                Sum = sortNum[i] + sortNum[left] + sortNum[right]
                if Sum == target:
                    return Sum
                elif Sum > target:
                    right -= 1
                else:
                    left += 1
                closest = Sum if abs(Sum - target) < abs(closest - target) else closest 
                
        return closest
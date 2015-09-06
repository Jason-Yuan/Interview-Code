# Greedy O(n)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        farthest = nums[0]
        for i in range(1, len(nums) - 1):
            if i <= farthest and farthest <= nums[i] + i:
                farthest = nums[i] + i
        return farthest >= len(nums) - 1


# DP not best answer O(n^2)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can = [False for i in range(len(nums))]
        can[0] = True
        for i in range(1, len(nums)):
            for j in range(0, i):
                if can[j] and nums[j] + j >= i:
                    can[i] = True
                    break
        return can[len(nums) - 1]
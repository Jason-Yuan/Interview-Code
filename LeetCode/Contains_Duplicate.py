# Method 1
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# Method 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 0
            else:
                map[num] += 1
        
        res = False
        for key, value in map.iteritems():
            if value > 0:
                res = True
            
        return res if res else False

# Method 3
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
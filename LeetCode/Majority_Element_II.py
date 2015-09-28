class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                candidate1 = num
            elif count2 == 0:
                count2 += 1
                candidate2 = num
            else:
                count1 -= 1
                count2 -= 1
                
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1
                
        result = []
        if count1 > len(nums) / 3:
            result.append(candidate1)
        if count2 > len(nums) / 3:
            result.append(candidate2)
        return result
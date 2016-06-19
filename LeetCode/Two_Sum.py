class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i, num in enumerate(nums):
            if num not in index:
                index[num] = [i]
            else:
                index[num].append(i)
                
        sortedNums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < j:
            if sortedNums[i] + sortedNums[j] == target:
                if sortedNums[i] == sortedNums[j]:
                    return [index[sortedNums[i]][0], index[sortedNums[i]][1]]
                else:
                    res = [index[sortedNums[i]][0], index[sortedNums[j]][0]]
                    return sorted(res)
            elif sortedNums[i] + sortedNums[j] > target:
                j -= 1
            else:
                i += 1
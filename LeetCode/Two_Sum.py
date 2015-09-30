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
                index[num] = [i+1]
            else:
                index[num].append(i+1)
            
        numsSorted = sorted(nums)
        start, end = 0, len(numsSorted) - 1
        while start < end:
            if numsSorted[start] + numsSorted[end] == target:
                if numsSorted[start] == numsSorted[end]:
                    return sorted(index[numsSorted[start]])
                else:
                    res = [index[numsSorted[start]][0], index[numsSorted[end]][0]]
                    return sorted(res)
            elif numsSorted[start] + numsSorted[end] > target:
                end -= 1
            else:
                start += 1
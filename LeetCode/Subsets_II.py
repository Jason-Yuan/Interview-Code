class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        else:
            nums.sort()
            result = [[]]
            self.subsetRecur(nums, 0, [], result)
            return result
            
    def subsetRecur(self, List, pos, path, result):
        for i in range(pos, len(List)):
            if i == pos:
                result.append(path + [List[i]])
            elif List[i] == List[i - 1]:
                continue
            else:
                result.append(path + [List[i]])
            self.subsetRecur(List, i + 1, path + [List[i]], result)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        flags = [False] * len(nums)
        
        self.permuteForReal(sorted(nums), result, flags, [])
        
        return result

    def permuteForReal(self, num, output, flags, path):
        if len(path) == len(num):
            output.append(path[:])
            return
         
        for i in range(len(num)):
            if not flags[i]:
                if i > 0 and not flags[i-1] and num[i] == num[i-1]:
                    continue
                path.append(num[i])
                flags[i] = True
                self.permuteForReal(num, output, flags, path)
                path.pop()
                flags[i] = False
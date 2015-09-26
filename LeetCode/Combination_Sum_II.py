class Solution(object):
    def helper(self, candidates, target, path, index, result):
        if target == 0:
            result.append(path[:])
            return
        prev = -1
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            if prev != -1 and prev == candidates[i]:
                continue
            self.helper(candidates, target - candidates[i], path+[candidates[i]], i+1, result)
            prev = candidates[i]
            
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if not candidates:
            return result
        
        candidates.sort()    
        self.helper(candidates, target, [], 0, result)
        return result
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return -1
          
        xor = 0 
        for item in nums:
            xor ^= item
        
        lastBit = xor - (xor & xor - 1)    
        group1, group2 = 0, 0
        for item in nums:
            if lastBit & item == 0:
                group1 ^= item
            else:
                group2 ^= item
                
        res = []
        res.append(group1)
        res.append(group2)
        return res
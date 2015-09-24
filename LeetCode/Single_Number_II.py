class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos, threes = 0, 0, 0
        for item in nums:
            twos |= ones & item      #hold item which occur twice
            ones ^= item           #hold item which occur once
            threes = ones & twos     #hold item which occur three times

            ones ^= threes         #once some item occur three items, reset ones
            twos ^= threes         #once some item occur three items, reset twos
        return ones
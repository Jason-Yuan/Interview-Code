class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or k < 1:
            pass
        else:
            if len(nums) > 1:
                k %= len(nums)
                self.reverseArray(nums, 0, len(nums) - 1 - k)
                self.reverseArray(nums, len(nums) - k, len(nums) - 1)
                self.reverseArray(nums, 0, len(nums) - 1)

    def reverseArray(self, array, start, end):
        while start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
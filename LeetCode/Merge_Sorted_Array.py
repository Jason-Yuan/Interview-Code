class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        lastNum1 = m - 1
        lastNum2 = n - 1
        lastRes = len(nums1) - 1
        while lastNum1 >= 0 and lastNum2 >= 0:
            if nums1[lastNum1] >= nums2[lastNum2]:
                nums1[lastRes] = nums1[lastNum1]
                lastNum1 -= 1
                lastRes -= 1
            else:
                nums1[lastRes] = nums2[lastNum2]
                lastNum2 -= 1
                lastRes -= 1
        while lastNum2 >= 0:
            nums1[lastRes] = nums2[lastNum2]
            lastNum2 -= 1
            lastRes -= 1
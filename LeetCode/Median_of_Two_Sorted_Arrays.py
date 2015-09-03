class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.KthNumber(nums1, nums2, n / 2 + 1)
        else:
            return (self.KthNumber(nums1, nums2, n / 2) + self.KthNumber(nums1, nums2, n / 2 + 1)) / 2.0
        
    def KthNumber(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]
        elif len(B) == 0:
            return A[k - 1]
        elif k == 1:
            return min(A[0], B[0])
            
        a = A[k / 2 - 1] if k / 2 <= len(A) else None
        b = B[k / 2 - 1] if k / 2 <= len(B) else None
        
        if b is None or (a is not None and a < b):
            return self.KthNumber(A[k / 2:], B, k - k / 2)
        else:
            return self.KthNumber(A, B[k / 2:], k - k / 2)
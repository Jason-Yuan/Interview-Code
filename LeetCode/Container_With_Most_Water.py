class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        if not height or len(height) < 2:
            return res
            
        left, right = 0, len(height) - 1
        res = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1
        return res
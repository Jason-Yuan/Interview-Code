# method 1, two pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

# method 2
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        MaxIndex = -1
        MaxHeight = -1
        for i in range(0, len(height)):
            if height[i] > MaxHeight:
                MaxHeight = height[i]
                MaxIndex = i
                
        prev = 0
        for i in range(0, MaxIndex):
            if height[i] > prev:
                water += (height[i] - prev) * (MaxIndex - i)
                prev = height[i]
            water -= height[i]
            
        prev = 0
        for i in range(len(height) - 1, MaxIndex, -1):
            if height[i] > prev:
                water += (height[i] - prev) * (i - MaxIndex)
                prev = height[i]
            water -= height[i]
            
        return water 
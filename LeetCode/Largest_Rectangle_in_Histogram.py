class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
            
        res = 0
        stack = []
        height.append(-1)
        for i in range(len(height)):
            current = height[i]
            while len(stack) != 0 and current <= height[stack[-1]]:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                stack = stack[:-3] +['#']
        return len(stack) == 1 and stack[-1] == "#"
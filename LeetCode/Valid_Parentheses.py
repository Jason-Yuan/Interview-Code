class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        balanced = True
        index = 0
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in "([{":
                stack.append(symbol)
            else:
                if len(stack) == 0:
                    balanced = False
                else:
                    top = stack.pop()
                    if not self.matches(top,symbol):
                       balanced = False
            index = index + 1
        if balanced and len(stack) == 0:
            return True
        else:
            return False

    def matches(self, open, close):
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)
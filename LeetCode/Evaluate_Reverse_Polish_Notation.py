class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = "+-*/"
        for str in tokens:
            if str not in operators:
                stack.append(int(str))
            else:
                a = stack.pop()
                b = stack.pop()
                if str == "+":
                    stack.append(a + b)
                elif str == "-":
                    stack.append(b - a)
                elif str == "*":
                    stack.append(a * b)
                elif str == "/":
                    if a * b < 0 and b % a != 0:
                        stack.append(b / a + 1)
                    else:
                        stack.append(b / a)
        if not stack:
            return 0
        return stack.pop()
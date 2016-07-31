# method 1
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

# method 2
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        elements = list(s)
        left, right = 0, len(elements) - 1
        while left < right:
            elements[left], elements[right] = elements[right], elements[left]
            left += 1
            right -= 1
            
        return "".join(elements)
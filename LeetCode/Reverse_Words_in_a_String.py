class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = s[::-1]
        temp_list = temp.split()
        ret = ""
        for word in temp_list:
            ret += word[::-1]
            ret += " "
        return ret[:-1]
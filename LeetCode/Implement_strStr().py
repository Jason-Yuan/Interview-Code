class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == None or needle == None or len(haystack) < len(needle):
            return -1
        if haystack == needle or needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            flag = True
            res = i
            for char in needle:
                if char == haystack[i]:
                    i += 1
                else:
                    flag = False
            if flag:
                return res
        return -1
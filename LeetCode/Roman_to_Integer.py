class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = val[s[-1]]

        for i in range(len(s) - 1):
            if val[s[i]] < val[s[i + 1]]:
                ans -= val[s[i]]
            else:
                ans += val[s[i]]

        return ans
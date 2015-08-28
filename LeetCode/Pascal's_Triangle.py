class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                temp = [1]
                for j in range(1, len(res[-1])):
                    temp.append(res[-1][j] + res[-1][j-1])
                temp.append(1)
                res.append(temp)
        return res
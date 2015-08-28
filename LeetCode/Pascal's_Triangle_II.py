class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return 
        elif rowIndex == 0:
            return [1]
        prevRow = self.getRow(rowIndex -1)
        mid = []
        for i in range(len(prevRow) - 1):
            mid.append(prevRow[i] + prevRow[i+1])
        return [1] + mid + [1]
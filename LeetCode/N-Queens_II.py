class Solution(object):
    def search(self, n, cols, result):
        if len(cols) == n:
            result[0] += 1
            return
        
        for col in range(n):
            if not self.isValid(cols, col):
                continue
            cols.append(col)
            self.search(n, cols, result)
            cols.pop()
            
    def isValid(self, cols, col):
        currentRowNumber = len(cols)
        for i in range(currentRowNumber):
            # same column
            if cols[i] == col:
                return False
            # left-top to right-bottom
            if i - cols[i] == currentRowNumber - col:
                return False
            # right-top to left-bottom
            if i + cols[i] == currentRowNumber + col:
                return False
        return True
            
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        cols = []
        result = [0]
        self.search(n, cols, result)
        return result[0]
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        start_row = len(matrix) - 1
        start_col = 0
        while start_row >= 0 and start_col <= len(matrix[0]) - 1:
            if matrix[start_row][start_col] == target:
                return True
            elif matrix[start_row][start_col] > target:
                start_row -= 1
            else:
                start_col += 1
                
        return False
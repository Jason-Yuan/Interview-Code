class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
            
        row_start = 0
        row_end = len(matrix) - 1
        while row_start + 1 < row_end:
            mid = row_start + (row_end - row_start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                row_start = mid
            else:
                row_end = mid
        row = row_start
        if matrix[row_end][0] <= target:
            row = row_end
        
        col_start = 0
        col_end = len(matrix[0]) - 1
                
        while col_start + 1 < col_end:
            mid = col_start + (col_end - col_start) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                col_start = mid
            else:
                col_end = mid
                
        if matrix[row][col_start] == target or matrix[row][col_end] == target:
            return True
        return False
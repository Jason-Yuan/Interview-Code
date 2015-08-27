class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        img_size = len(matrix)
        for row in range(img_size/2):
		for col in range(row, img_size-row-1):
			temp = matrix[row][col]
			matrix[row][col] = matrix[img_size-col-1][row]
			matrix[img_size-col-1][row] = matrix[img_size-row-1][img_size-col-1]
			matrix[img_size-row-1][img_size-col-1] = matrix[col][img_size-row-1]
			matrix[col][img_size-row-1] = temp
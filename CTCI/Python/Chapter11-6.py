##############################################################################################################################
# Ideas:	1. Start from left-right conner
#       	2. if the target > left-right conner, eliminate current row, move to below one
#           3. if the target < left-right conner, eliminate current col, move to left one
# Time Complexity: O(m + n)
# Space Complexity: O(1)
##############################################################################################################################

def searchMatrix(matrix, target):
	if len(matrix) < 1:
		return False

	row = 0
	col = len(matrix[0]) - 1
	while row < len(matrix[0]) and col >= 0:
		if matrix[row][col] == target:
			return (row, col)
		elif matrix[row][col] > target:
			col -= 1
		else:
			row += 1

	return False

def printMatrix(matrix):
	for row in matrix:
		print row

##############################################################################################################################

def main():
	a = [[1,3,5], [2, 4, 7], [5, 6, 9]]
	target = 2
	print "Find {} in matrix".format(target)
	printMatrix(a)
	print "The result is: {}".format(searchMatrix(a, target))

if __name__ == '__main__':
	main()
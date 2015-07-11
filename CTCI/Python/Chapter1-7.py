# define a print matrix method
def ShowMatrix(matrix):
	for row in matrix:
		print row
# end define

##############################################################################################################################
# Method 1 
# Ideas: Loop each elements in the M*N matrix, and keep record the row number and column number the 0 element
#        Loop another time and change the corresponding rows and columns to be 0
#        Use two array to keep record
# Time Complexity: O(m*n)
# Space Complexity: O(m+n)
##############################################################################################################################

def SetMatrixZero1(matrix):
	zero_col = []
	zero_row = []

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 0:
				zero_row.append(row)
				zero_col.append(col)

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if row in zero_row or col in zero_col:
				matrix[row][col] = 0

	return matrix

##############################################################################################################################
# Method 2
# Ideas: Loop each elements in the M*N matrix, and keep record the row number and column number the 0 element
#        Loop another time and change the corresponding rows and columns to be 0
#        Use the first row and first column to keep record, and we only need to flag to indicate if first row
#        and first column should all be zero
#        e.g.   if matrix[m][n] == 0 we set matrix[0][n] == 0 and matrix[m][0] == 0 since they will be 0 finally, the flag is 
#               used to indicate the other elemtnets in first row and first column should be 0 or not 
# Time Complexity: O(m*n)
# Space Complexity: O(1)
##############################################################################################################################

def SetMatrixZero2(matrix):
	first_row = False
	first_col = False

	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			first_row = True
	for j in range(len(matrix[0])):
		if matrix[0][j] == 0:
			first_col = True

	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 0:
				matrix[0][col] = 0
				matrix[row][0] = 0

	for row in range(1, len(matrix)):
		for col in range(1, len(matrix[0])):
			if matrix[row][0] == 0 or matrix[0][col] == 0:
				matrix[row][col] = 0

	if first_row:
		for i in range(len(matrix)):
			matrix[i][0] = 0;

	if first_col:
		for j in range(len(matrix[0])):
			matrix[0][j] = 0;			

	return matrix

##############################################################################################################################

def main():
	matrix1 = [ [1, 0, 3, 8, 9],
	          [3, 7, 8, 6, 1],
 		      [4, 1, 3, 5, 0] ]

 	matrix2 = [ [1, 0, 3, 8, 9],
 		      [3, 7, 8, 6, 1],
 		      [4, 1, 3, 5, 0] ]

 	print "Set Matrix zero method 1:"
 	ShowMatrix(SetMatrixZero1(matrix1))

 	print "Set Matrix zero method 2:"
	ShowMatrix(SetMatrixZero2(matrix2))

if __name__ == '__main__':
	main()
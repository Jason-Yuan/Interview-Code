##############################################################################################################################
# Method 1
# Ideas: If HasWon() method needed to be called for many times, we should store all the possible board with the result
#        in a hashmap, then we can have O(1) time complexity
#        We need to method to convert board to an integer
# Time Complexity: O(1)
# Space Complexity: O(3^(n^2))
##############################################################################################################################

def hasWon1(board):
	key = convertBoardToInt(board)
	return winnerHashtable[key]

def convertBoardToInt(board):
	factor = 1
	sum = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			v = 0
			if board[i][j] == "x":
				v = 1
			if board[i][j] == "o":
				v = 2
			sum += v * factor
			factor *= 3
	return sum

##############################################################################################################################
# Method 2
# Ideas: 1. Check rows
#        2. Check columns
#        3. Check diagonal and reverse diagonal
# Time Complexity: O(n^2)
# Space Complexity: O(1)
##############################################################################################################################

def hasWon2(board):
	if not board:
		return False

	# Check row
	for i in range(len(board)):
		col = 0
		if board[i][col] != ' ':
			while col < len(board[0]) - 1:
				if board[i][col] != board[i][col + 1]:
					break
				col += 1
			if col == len(board[0]) - 1:
				return board[i][0]

	# Check col
	for i in range(len(board[0])):
		row = 0
		if board[row][i] != ' ':
			while row < len(board) - 1:
				if board[row][i] != board[row + 1][i]:
					break
				row += 1
			if row == len(board) - 1:
				return board[0][i]

	# Check diagonal and reverse diagonal
	i = 0
	diagonal = reverseDiagonal = True
	while i < len(board) - 1:
		if board[i][i] != board[i + 1][i + 1]:
			diagonal = False
		if board[i][len(board[0]) - 1 - i] != board[i + 1][len(board[0]) - i - 2]:
			reverseDiagonal = False
		i += 1

	if diagonal:
		return board[0][0]
	if reverseDiagonal:
		return board[0][len(board[0]) - 1]

	return "Nobody"

def printBoard(board):
	for row in board:
		for i in range(len(row) - 1):
			print row[i],
		print row[len(row) - 1]

##############################################################################################################################

def main():
	board1 = [['O', 'X', 'X'], ['X', 'X', 'O'], ['X', ' ', ' ']]
  	board2 = [[' ', 'X', ' ', ' '], ['O', 'X', 'O', 'O'], ['O', 'X', 'X', 'X'], [' ', 'X', 'O', 'O']]
  	printBoard(board1)
  	print "Result: {} won.".format(hasWon2(board1))
  	printBoard(board2)
  	print "Result is {} won.".format(hasWon2(board2))

if __name__ == '__main__':
	main()
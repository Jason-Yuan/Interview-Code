class Solution(object):
    def __init__(self):
        self.word = ""
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        for row_num in range(len(board)):
            for col_num in range(len(board[0])):
                if self.search(board, row_num, col_num, 0):
                    return True
                
        return False
        
    def search(self, board, x, y, pos):
        if self.word[pos] == board[x][y]:
            if pos == len(self.word) - 1:
                return True
            else:
                temp = board[x][y]
                board[x][y] = None
                if x + 1 < len(board) and self.search(board, x + 1, y, pos + 1):
                    return True
                if x - 1 >= 0 and self.search(board, x - 1, y, pos + 1):
                    return True
                if y + 1 < len(board[0]) and self.search(board, x, y + 1, pos + 1):
                    return True
                if y - 1 >= 0 and self.search(board, x, y - 1, pos + 1):
                    return True
                board[x][y] = temp
                return False
        else:
            return False
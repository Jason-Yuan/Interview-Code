import Queue
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x < 0 or x > height-1 or y < 0 or y > width-1 or board[x][y] != "O":
                return
            MyQueue.put((x, y))
            board[x][y] = "D"
            
        def bfs(x, y):
            if board[x][y] == "O":
                fill(x, y)
                
            while not MyQueue.empty():
                current = MyQueue.get()
                i, j = current[0], current[1]
                fill(i+1, j)
                fill(i-1, j)
                fill(i, j+1)
                fill(i, j-1)
                
        if len(board) == 0:
            return
        
        height, width, MyQueue = len(board), len(board[0]), Queue.Queue()
        for i in range(width):
            bfs(0, i)
            bfs(height - 1, i)
        
        for j in range(1, height - 1):
            bfs(j, 0)
            bfs(j, width - 1)
            
        for i in range(height):
            for j in range(width):
                if board[i][j] == "D":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
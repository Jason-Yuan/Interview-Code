##############################################################################################################################
# Ideas: Recursion    
# Time Complexity: O(n^2)
# Space Complexity: O(n)
##############################################################################################################################

class nQueens(object):
    def __init__(self):
        self.results = []

    def placeQueens(self, n = 8, row = 0, temp = None):
        if temp is None:
            temp = []

        if row == n:
            self.results.append(temp[:])
            return

        for i in range(n):
            if self.isValidPosition(row, i, temp):
                temp.append(i)
                self.placeQueens(n, row + 1, temp)
                temp.pop()

        return self.results

    def isValidPosition(self, row, col, temp):
        for i in range(row):
            if temp[i] == col:
                return False

            if abs(temp[i] - col) == row - i:
                return False

        return True

##############################################################################################################################

def main():
    result = nQueens()
    print "Number of different boards: ", len(result.placeQueens(8))

if __name__ == '__main__':
    main()